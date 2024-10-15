
import requests
import json
from datetime import datetime
from sqlalchemy import text, create_engine
import os
from pandas import pd


def fetch_and_process_data(csv_file_path, connection_string, table_name):
    df = pd.read_csv(csv_file_path, low_memory=False)

    df['VervotechId'] = df['UnicaId']
    df['last_update'] = pd.NA
    df['UpdateDateFormat'] = pd.NA

    columns_to_insert = ['VervotechId', 'Name', 'Latitude', 'Longitude', 'AddressLine1', 'AddressLine2', 'CityName', 'StateName',
                         'StateCode', 'CountryName', 'CountryCode', 'PostalCode', 'Rating', 'PropertyType',
                         'ChainName', 'ChainCode', 'BrandName', 'CityCode', 'CityLocationId', 'MasterCityName',
                         'LocationIds', 'Phones', 'Emails', 'Fax', 'Website', 'AirportCodes', 'TrainStations',
                         'ProviderHotelId', 'ProviderFamily', 'GooglePlusCode', 'GooglePlaceId', 'Tags']

    engine = create_engine(connection_string)

    try:
        for i, row in df[columns_to_insert].iterrows():
            single_row_df = pd.DataFrame([row])
            single_row_df.to_sql(table_name, con=engine, if_exists='append', index=False)
            print(f"Upload successful: {i + 1} row(s) inserted.")
        print("Upload successfully complete.")
    except Exception as e:
        print(f"An error occurred: {e}")


def save_data_to_db(data, engine, table_name):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
    log = ""
    insert_stmt = text(f"""
        INSERT INTO {table_name} (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ChannelIds, ProviderLocationCode, status)
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId,  :ProviderFamily, :ChannelIds, :ProviderLocationCode, :status)
        ON DUPLICATE KEY UPDATE
            last_update = :last_update,
            VervotechId = :VervotechId,
            UpdateDateFormat = :UpdateDateFormat,
            ProviderHotelId = :ProviderHotelId,
            ProviderFamily = :ProviderFamily,
            ChannelIds = :ChannelIds,
            ProviderLocationCode = :ProviderLocationCode,
            status = :status
    """)

    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            for record in data:
                connection.execute(insert_stmt, {
                    'last_update': current_time,
                    'VervotechId': record.get('VervotechId'),
                    'UpdateDateFormat': record.get('UpdateDateFormat') or None,
                    'ProviderHotelId': record.get('ProviderHotelId'),
                    'ProviderFamily': record.get('ProviderName'),
                    'ChannelIds': None,
                    'ProviderLocationCode': record.get('ProviderLocationCode') or None,
                    'status' : "new_data"
                })
                log += f"Record with VervotechId {record.get('VervotechId')} inserted/updated successfully.\n"
            transaction.commit()
            log += "Transaction committed successfully.\n"
        except Exception as e:
            transaction.rollback()
            log += f"Transaction failed: {e}\n"
    return log

def update_mapping_fetch_data(url, params, headers, engine, table_name):
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            f"Error: Received status code {response.status_code}\n"
            f"Response: {response.text}\n"
            break

        try:
            response_data = response.json()
        except ValueError as e:
            f"JSON decode error: {e}\n"
            f"Response content: {response.text}\n"
            break

        if 'Mappings' in response_data and response_data['Mappings']:
            new_data = response_data['Mappings']
            if "ResumeKey" in response_data:
                save_data_to_db(new_data, engine, table_name)
                params['resumeKey'] = response_data["ResumeKey"]
            else:
                "No more ResumeKey found. Fetching complete.\n"
                break
        else:
            "No data found in response.\n"
            break




def new_mapping_fetch_data(url, params, headers, engine, table_name):
    while True:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            break
        
        try:
            response_data = response.json()
            # print("Full API Response:", json.dumps(response_data, indent=4)) 
        except ValueError as e:
            print(f"JSON decode error: {e}")
            print(f"Response content: {response.text}")
            break
        
        if 'Mappings' in response_data and response_data['Mappings']:
            new_data = response_data['Mappings']  
            
            if "ResumeKey" in response_data:
                # print(f"Continuing to fetch data with ResumeKey: {response_data['ResumeKey']}")
                save_data_to_db(new_data, engine, table_name)
                # Update the params to include the new ResumeKey for the next request
                params['resumeKey'] = response_data["ResumeKey"]
            else:
                # If no ResumeKey, end the loop
                print("No more ResumeKey found. Fetching complete.")
                break
        else:
            print("No data found in response.")
            break



def update_vervotech_mapping_data(engine):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')

    insert_into_table_3_stmt = text(f"""
        INSERT INTO vervotech_mapping
        (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ModifiedOn, ChannelIds, ProviderLocationCode, status)
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId, :ProviderFamily, :ModifiedOn, :ChannelIds, :ProviderLocationCode, 'update successful')
    """)

    check_existing_record_stmt = text(f"""
        SELECT COUNT(*) FROM vervotech_mapping
        WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId
    """)

    def update_mapping_from_table(table_name):
        update_status_stmt = text(f"""
            UPDATE {table_name}
            SET status = 'Update data successful'
            WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId
        """)

        select_new_data_stmt = text(f"""
            SELECT * FROM {table_name}
            WHERE status = 'new_data'
        """)
        
        with engine.connect() as connection:
            records = connection.execute(select_new_data_stmt).mappings().all()

            for record in records:
                result = connection.execute(check_existing_record_stmt, {
                    'VervotechId': record['VervotechId'],
                    'ProviderHotelId': record['ProviderHotelId']
                }).scalar()

                if result > 0:
                    print(f"Record with VervotechId {record['VervotechId']} and ProviderHotelId {record['ProviderHotelId']} already exists in vervotech_mapping. Skipping.")
                else:
                    connection.execute(insert_into_table_3_stmt, {
                        'last_update': current_time,
                        'VervotechId': record['VervotechId'],
                        'UpdateDateFormat': record['UpdateDateFormat'] or None,
                        'ProviderHotelId': record['ProviderHotelId'],
                        'ProviderFamily': record['ProviderFamily'],
                        'ModifiedOn': current_time,
                        'ChannelIds': record['ChannelIds'] or None,
                        'ProviderLocationCode': record['ProviderLocationCode'] or None
                    })
                    print(f"Inserted record with VervotechId {record['VervotechId']} into vervotech_mapping.")

                    connection.execute(update_status_stmt, {
                        'VervotechId': record['VervotechId'],
                        'ProviderHotelId': record['ProviderHotelId']
                    })
                    print(f"Updated status to 'Update data successful' in table {table_name} for VervotechId {record['VervotechId']}.")

    # Update from both vervotech_hotel_map_new (table 1) and vervotech_hotel_map_update (table 2)
    update_mapping_from_table('vervotech_hotel_map_new')
    update_mapping_from_table('vervotech_hotel_map_update')



def save_json_file(engine):
    # Directory to save JSON files
    # json_dir = "D:/data_validation/logs/json_file"
    json_dir = "D:/data_validation/logs/json_file"
    os.makedirs(json_dir, exist_ok=True)  

    fetch_data_stmt = text("""
        SELECT VervotechId, ProviderHotelId, ProviderFamily, ProviderLocationCode 
        FROM vervotech_mapping
    """)

    with engine.connect() as connection:
        records = connection.execute(fetch_data_stmt).mappings().all()

        # Prepare a dictionary to hold data grouped by VervotechId
        data_to_save = {}

        for record in records:
            vervotech_id = record['VervotechId']
            # If VervotechId is not in the dictionary, create an empty list for it
            if vervotech_id not in data_to_save:
                data_to_save[vervotech_id] = []
            # Append the record data to the corresponding VervotechId key
            data_to_save[vervotech_id].append({
                'VervotechId': record['VervotechId'],
                'ProviderHotelId': record['ProviderHotelId'],
                'ProviderFamily': record['ProviderFamily'],
                'ProviderLocationCode': record['ProviderLocationCode']
            })

        # Save each VervotechId's data to a separate JSON file
        for vervotech_id, entries in data_to_save.items():
            json_file_path = os.path.join(json_dir, f"{vervotech_id}.json")
            with open(json_file_path, 'w') as json_file:
                json.dump(entries, json_file, indent=4)
            print(f"Saved data for VervotechId {vervotech_id} to {json_file_path}")


