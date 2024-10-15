import requests
import json
import os
from datetime import datetime
from sqlalchemy import text, create_engine, exc



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
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId, :ProviderFamily, :ModifiedOn, :ChannelIds, :ProviderLocationCode, 'Update')
    """)

    check_existing_record_stmt = text(f"""
        SELECT COUNT(*) FROM vervotech_mapping
        WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId AND ProviderFamily = :ProviderFamily
    """)

    update_null_status_stmt = text(f"""
        UPDATE vervotech_mapping
        SET status = 'Update'
        WHERE status IS NULL
    """)

    def update_mapping_from_table(table_name):
        update_status_skipping_stmt = text(f"""
            UPDATE {table_name}
            SET status = 'Skipping data'
            WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId AND ProviderFamily = :ProviderFamily
        """)

        update_status_successful_stmt = text(f"""
            UPDATE {table_name}
            SET status = 'Update data successful'
            WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId AND ProviderFamily = :ProviderFamily
        """)

        select_new_data_stmt = text(f"""
            SELECT * FROM {table_name}
            WHERE status = 'new_data'
        """)

        with engine.begin() as connection:  
            try:
                # Fetch records with status 'new_data'
                records = connection.execute(select_new_data_stmt).mappings().all()

                for record in records:
                    result = connection.execute(check_existing_record_stmt, {
                        'VervotechId': record['VervotechId'],
                        'ProviderHotelId': record['ProviderHotelId'],
                        'ProviderFamily': record['ProviderFamily']
                    }).scalar()

                    if result > 0:
                        print(f"Record with VervotechId {record['VervotechId']} and ProviderHotelId {record['ProviderHotelId']} already exists in vervotech_mapping. Skipping.")
                        connection.execute(update_status_skipping_stmt, {
                            'VervotechId': record['VervotechId'],
                            'ProviderHotelId': record['ProviderHotelId'],
                            'ProviderFamily': record['ProviderFamily']
                        })
                        print(f"Updated status to 'Skipping data' in table {table_name} for VervotechId {record['VervotechId']}.")
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
                        print(f"Inserted record with VervotechId {record['VervotechId']} into vervotech_mapping (status: 'Update').")

                        # Update the source table status to 'Update data successful'
                        connection.execute(update_status_successful_stmt, {
                            'VervotechId': record['VervotechId'],
                            'ProviderHotelId': record['ProviderHotelId'],
                            'ProviderFamily': record['ProviderFamily']
                        })
                        print(f"Updated status to 'Update data successful' in table {table_name} for VervotechId {record['VervotechId']}.")
            
            except exc.SQLAlchemyError as e:
                print(f"Error occurred during database operation: {e}")
                raise

    # Process updates from both tables
    update_mapping_from_table('vervotech_hotel_map_new')
    update_mapping_from_table('vervotech_hotel_map_update')

    with engine.begin() as connection:
        connection.execute(update_null_status_stmt)
        print("Updated existing NULL statuses in vervotech_mapping to 'Update'.")




def save_json_file(engine):
    # Directory to save JSON files
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
            if vervotech_id not in data_to_save:
                data_to_save[vervotech_id] = []
            data_to_save[vervotech_id].append({
                'VervotechId': record['VervotechId'],
                'ProviderHotelId': record['ProviderHotelId'],
                'ProviderFamily': record['ProviderFamily'],
                'ProviderLocationCode': record['ProviderLocationCode']
            })

        for vervotech_id, entries in data_to_save.items():
            json_file_path = os.path.join(json_dir, f"{vervotech_id}.json")
            
            # If the file already exists, load its content and update
            if os.path.exists(json_file_path):
                with open(json_file_path, 'r') as json_file:
                    existing_data = json.load(json_file)
                
                # Create a set for existing unique identifiers to avoid duplicates
                existing_set = {(entry['ProviderHotelId'], entry['ProviderFamily'], entry['ProviderLocationCode']) for entry in existing_data}
                
                # Filter out entries that already exist
                new_entries = [
                    entry for entry in entries
                    if (entry['ProviderHotelId'], entry['ProviderFamily'], entry['ProviderLocationCode']) not in existing_set
                ]
                
                # Update existing data with new unique entries
                existing_data.extend(new_entries)
                entries = existing_data

            # Save the updated entries back to the JSON file
            with open(json_file_path, 'w') as json_file:
                json.dump(entries, json_file, indent=4)
            print(f"Saved data for VervotechId {vervotech_id} to {json_file_path}")


