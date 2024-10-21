import requests
import json
import os
from datetime import datetime
from sqlalchemy import text, exc
from api_call.payload import get_content_by_provider_hotel_ids_create_payload
from api_call.headers import get_content_by_provider_hotel_ids_headers
from env_request.request_env import load_environment_variables_local



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
                        # Check if any of the key fields have changed
                        if (record['ProviderLocationCode'] != existing_record['ProviderLocationCode'] or
                            record['ProviderHotelId'] != existing_record['ProviderHotelId'] or
                            record['ProviderFamily'] != existing_record['ProviderFamily']):
                            
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



def update_hotel_mapping_with_content(url, engine, table_name):
    """
    Updates all rows in the table where content_update_status is not 'Done'.
    For each row, it fetches the data from the API and updates the table with hotel details.
    
    Args:
        url (str): The API URL.
        headers (dict): The headers required for the API request.
        engine (SQLAlchemy engine): The SQLAlchemy engine object connected to the database.
        table_name (str): The name of the table to update in the database.
    """
    all_successful = True
    with engine.connect() as connection:
        try:
            select_query = text(f"""
                SELECT Id, ProviderHotelId, ProviderFamily 
                FROM {table_name} 
                WHERE content_update_status IS NULL OR content_update_status != 'Done'
            """)
            result = connection.execute(select_query)
            rows = result.fetchall()  # Fetch all rows at once

            # Check if any rows were returned
            if not rows:
                print("No records found where content_update_status is not 'Done'.")
                return  # Exit the function if no rows are found

            for row in rows:
                record_id, provider_hotel_id, provider_family = row  # Unpack the tuple

                payload = get_content_by_provider_hotel_ids_create_payload(provider_hotel_id=provider_hotel_id, provider_family=provider_family)

                # Update the hotel data and check for success
                success = update_with_provider_hotel_ids(url, payload, engine, table_name, record_id)

                if not success:
                    all_successful = False
                    print(f"Failed to update content for record {record_id}")

                print(f"Update: ------------------------ {record_id}")

            if all_successful:
                print("All update content successfully done")

        except exc.SQLAlchemyError as e:
            print(f"Database error occurred: {e}")

        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")



def update_with_provider_hotel_ids(url, payload, engine, table_name, record_id):
    """ 
    Fetches data from the API using the provided URL, payload, and headers, 
    and updates the specified database table with the hotel data using raw SQL queries.

    Args:
        url (str): The API URL.
        payload (str): The JSON payload for the API request.
        headers (dict): The headers required for the API request.
        engine (SQLAlchemy engine): The SQLAlchemy engine object connected to the database.
        table_name (str): The name of the table to update in the database.
        record_id (int): The record Id to update in the database.
    """
    # Open a new database connection using the engine
    with engine.connect() as connection:
        trans = connection.begin()
        try:
            env_vars = load_environment_variables_local()
            api_key = env_vars['vervotech_api_key']
            headers = get_content_by_provider_hotel_ids_headers(api_key) 
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

                        geo_code = provider_hotel.get('GeoCode', {})
                        lat = geo_code.get('GeoCode', {}).get('Lat')
                        long = geo_code.get('GeoCode', {}).get('Long')
                        country_code = provider_hotel.get('Contact', {}).get('Address', {}).get('CountryCode')
                        last_update = datetime.now()
                        content_update_status = 'Done'

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
                                last_update = :last_update,
                                content_update_status = :content_update_status
                            WHERE Id = :record_id
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
                            'content_update_status': content_update_status,
                            'record_id': record_id
                        })
                        print(f"Update successfully  this provider hotel Id {provider_hotel_id}")
                trans.commit()
                return True
            else:
                print(f"Failed to fetch data for record {record_id}. Status Code: {response.status_code}")
                return False
        
        except exc.SQLAlchemyError as e:
            trans.rollback()
            print(f"Database error occurred: {e}")
            return False
        
        except requests.exceptions.RequestException as e:
            trans.rollback()
            print(f"Request error occurred: {e}")
            return False







