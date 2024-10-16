import requests
import json
import os
from datetime import datetime
from sqlalchemy import text, exc



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
            print(f"Vervotech {len(data)} data insert")
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
                print(f"vervotech {len(new_data)} data insert")
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
        SELECT VervotechId, ProviderHotelId, ProviderFamily, ProviderLocationCode
        FROM vervotech_mapping
        WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId AND ProviderFamily = :ProviderFamily
    """)

    def update_mapping_from_table(table_name):
        update_status_skipping_stmt = text(f"""
            UPDATE {table_name}
            SET status = 'Skipping data'
            WHERE VervotechId = :VervotechId 
            AND ProviderHotelId = :ProviderHotelId 
            AND ProviderFamily = :ProviderFamily
        """)

        update_status_successful_stmt = text(f"""
            UPDATE {table_name}
            SET status = 'Update data successful'
            WHERE VervotechId = :VervotechId 
            AND ProviderHotelId = :ProviderHotelId 
            AND ProviderFamily = :ProviderFamily
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
                    # Fetch the existing record from the database, using mappings() for dictionary-like access
                    existing_record = connection.execute(check_existing_record_stmt, {
                        'VervotechId': record['VervotechId'],
                        'ProviderHotelId': record['ProviderHotelId'],
                        'ProviderFamily': record['ProviderFamily'],
                    }).mappings().fetchone()

                    if existing_record:
                        # Compare if any of the key values (ProviderLocationCode) are different
                        if record['ProviderLocationCode'] != existing_record['ProviderLocationCode']:
                            print(f"Record with VervotechId {record['VervotechId']} has changed, updating.")
                            connection.execute(insert_into_table_3_stmt, {
                                'last_update': current_time,
                                'VervotechId': record['VervotechId'],
                                'UpdateDateFormat': record['UpdateDateFormat'] or None,
                                'ProviderHotelId': record['ProviderHotelId'],
                                'ProviderFamily': record['ProviderFamily'],
                                'ModifiedOn': current_time,
                                'ChannelIds': record['ChannelIds'] or None,
                                'ProviderLocationCode': record['ProviderLocationCode'] or None,
                                'status': 'Update'
                            })

                            # Update the source table status to 'Update data successful'
                            connection.execute(update_status_successful_stmt, {
                                'VervotechId': record['VervotechId'],
                                'ProviderHotelId': record['ProviderHotelId'],
                                'ProviderFamily': record['ProviderFamily']
                            })
                        else:
                            print(f"Record with VervotechId {record['VervotechId']} already exists with no changes. Skipping.")
                            connection.execute(update_status_skipping_stmt, {
                                'VervotechId': record['VervotechId'],
                                'ProviderHotelId': record['ProviderHotelId'],
                                'ProviderFamily': record['ProviderFamily']
                            })
                    else:
                        print(f"Inserting new record with VervotechId {record['VervotechId']}.")
                        connection.execute(insert_into_table_3_stmt, {
                            'last_update': current_time,
                            'VervotechId': record['VervotechId'],
                            'UpdateDateFormat': record['UpdateDateFormat'] or None,
                            'ProviderHotelId': record['ProviderHotelId'],
                            'ProviderFamily': record['ProviderFamily'],
                            'ModifiedOn': current_time,
                            'ChannelIds': record['ChannelIds'] or None,
                            'ProviderLocationCode': record['ProviderLocationCode'] or None,
                            'status': 'Update'
                        })

                        # Update the source table status to 'Update data successful'
                        connection.execute(update_status_successful_stmt, {
                            'VervotechId': record['VervotechId'],
                            'ProviderHotelId': record['ProviderHotelId'],
                            'ProviderFamily': record['ProviderFamily']
                        })

            except exc.SQLAlchemyError as e:
                print(f"Error occurred during database operation: {e}")
                raise

    # Process updates from both tables
    update_mapping_from_table('vervotech_hotel_map_new')
    update_mapping_from_table('vervotech_hotel_map_update')




def save_json_file(engine):
    # Directory to save JSON files
    # json_dir = "/var/www/hotelmap.gtrsystem.com"
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





def update_with_provider_hotel_ids(url, payload, headers, engine, table_name):
    """
    Fetches data from the API using the provided URL, payload, and headers, 
    and updates the specified database table with the hotel data using raw SQL queries.

    Args:
        url (str): The API URL.
        payload (str): The JSON payload for the API request.
        headers (dict): The headers required for the API request.
        engine (SQLAlchemy engine): The SQLAlchemy engine object connected to the database.
        table_name (str): The name of the table to update in the database.
    """
    # Open a new database connection using the engine
    with engine.connect() as connection:
        try:
            # Fetch data from the API
            response = requests.post(url, headers=headers, data=payload)
            
            if response.status_code == 200:
                data = response.json()
                hotels = data.get('Hotels', [])
                
                # Iterate over each hotel and update the table
                for hotel in hotels:
                    provider_hotels = hotel.get('ProviderHotels', [])
                    for provider_hotel in provider_hotels:
                        # Extract required data
                        hotel_name = provider_hotel.get('Name')
                        city = provider_hotel.get('Contact', {}).get('Address', {}).get('City')
                        country = provider_hotel.get('Contact', {}).get('Address', {}).get('Country')
                        lat = provider_hotel.get('GeoCode', {}).get('Lat')
                        long = provider_hotel.get('GeoCode', {}).get('Long')
                        country_code = provider_hotel.get('Contact', {}).get('Address', {}).get('CountryCode')
                        last_update = datetime.now()

                        # Extract ProviderHotelId to update the correct row
                        provider_hotel_id = provider_hotel.get('ProviderHotelId')
                        
                        # Create the raw SQL query for updating the table
                        update_query = text(f"""
                            UPDATE {table_name}
                            SET 
                                hotel_name = :hotel_name,
                                hotel_city = :city,
                                hotel_country = :country,
                                hotel_latitude = :lat,
                                hotel_longitude = :long,
                                country_code = :country_code,
                                last_update = :last_update
                            WHERE ProviderHotelId = :provider_hotel_id
                        """)
                        
                        # Execute the update query with bound parameters
                        connection.execute(update_query, {
                            'hotel_name': hotel_name,
                            'city': city,
                            'country': country,
                            'lat': lat,
                            'long': long,
                            'country_code': country_code,
                            'last_update': last_update,
                            'provider_hotel_id': provider_hotel_id
                        })
                        print("Update sucessfully")
            else:
                print(f"Failed to fetch data. Status Code: {response.status_code}")
        
        except exc.SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
        
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")

