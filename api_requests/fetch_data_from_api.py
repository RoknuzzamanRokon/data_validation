import requests
import json
import os
from datetime import datetime
from sqlalchemy import text, exc
from api_call.payload import get_content_by_provider_hotel_ids_create_payload
from api_call.headers import get_content_by_provider_hotel_ids_headers
from env_request.request_env import load_environment_variables_local
from sqlalchemy.orm import sessionmaker


def save_data_to_db(data, engine, table_name):
    """
    Saves or updates data in the database and logs each action.
    Immediately commits changes to reflect in the database after each record.
    """
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
    log = ""
    insert_stmt = text(f"""
        INSERT INTO {table_name} (last_update, VervotechId, ProviderHotelId, ProviderFamily, ChannelIds, ProviderLocationCode, status)
        VALUES (:last_update, :VervotechId, :ProviderHotelId,  :ProviderFamily, :ChannelIds, :ProviderLocationCode, :status)
        ON DUPLICATE KEY UPDATE
            last_update = :last_update,
            VervotechId = :VervotechId,
            ProviderHotelId = :ProviderHotelId,
            ProviderFamily = :ProviderFamily,
            ChannelIds = :ChannelIds,
            ProviderLocationCode = :ProviderLocationCode,
            status = :status
    """)

    with engine.connect() as connection:
        for record in data:
            try:
                connection.execute(insert_stmt, {
                    'last_update': current_time,
                    'VervotechId': record.get('VervotechId'),
                    'ProviderHotelId': record.get('ProviderHotelId'),
                    'ProviderFamily': record.get('ProviderName'),
                    'ChannelIds': json.dumps(record.get('ChannelIds')) if record.get('ChannelIds') else None,
                    'ProviderLocationCode': record.get('ProviderLocationCode') or None,
                    'status': "new_data"
                })
                connection.commit()
                log += f"Record with VervotechId {record.get('VervotechId')} inserted/updated successfully.\n"
                print(f"Record with VervotechId {record.get('VervotechId')} saved to database.")
            except Exception as e:
                connection.rollback()
                log += f"Failed to insert/update record with VervotechId {record.get('VervotechId')}: {e}\n"
                print(f"Error saving record with VervotechId {record.get('VervotechId')}: {e}")
    
    return log


def update_mapping_fetch_data(url, params, headers, engine, table_name):
    while True:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            break
        
        try:
            response_data = response.json()
            # print("Response data:", response_data) 
        except ValueError as e:
            print(f"JSON decode error: {e}")
            print(f"Response content: {response.text}")
            break
        
        if 'Mappings' in response_data and response_data['Mappings']:
            new_data = response_data['Mappings']
            # print("New data:", new_data)  # Debug: Print new data to be saved
            
            save_data_to_db(new_data, engine, table_name)
            
            if "ResumeKey" in response_data and response_data["ResumeKey"] is not None:
                params['resumeKey'] = response_data["ResumeKey"]
                # print(f"Continuing with ResumeKey: {response_data['ResumeKey']}")  
            else:
                print("No ResumeKey found or ResumeKey is None. Fetching complete.")
                break
        else:
            print("No data found in 'Mappings'.")
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
                params['resumeKey'] = response_data["ResumeKey"]
            else:
                # If no ResumeKey, end the loop
                print("No more ResumeKey found. Fetching complete.")
                break
        else:
            print("No data found in response.")
            break




        
# def update_vervotech_mapping_data(engine):
#     current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
#     def execute_statement(session, statement, parameters=None):
#         try:
#             result = session.execute(statement, parameters or {})
#             return result
#         except exc.SQLAlchemyError as e:
#             print(f"Error executing statement: {e}")
#             raise

#     insert_stmt = text("""
#         INSERT INTO vervotech_mapping
#         (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ModifiedOn, ChannelIds, ProviderLocationCode, status)
#         VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId, :ProviderFamily, :ModifiedOn, :ChannelIds, :ProviderLocationCode, 'Update')
#     """)

#     check_record_stmt = text("""
#         SELECT VervotechId, ProviderHotelId, ProviderFamily, ProviderLocationCode
#         FROM vervotech_mapping
#         WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId AND ProviderFamily = :ProviderFamily
#     """)

#     update_status_stmt_template = """
#         UPDATE {table_name}
#         SET status = :status
#         WHERE VervotechId = :VervotechId 
#         AND ProviderHotelId = :ProviderHotelId 
#         AND ProviderFamily = :ProviderFamily
#     """

#     def process_table_data(table_name):
#         select_stmt = text(f"""
#             SELECT * FROM {table_name}
#             WHERE status = 'new_data'
#         """)

#         Session = sessionmaker(bind=engine)
#         with Session() as session:
#             records = execute_statement(session, select_stmt).mappings().all()
#             if not records:
#                 print(f"No new records found in {table_name}.")
#                 return

#             for record in records:
#                 existing_record = execute_statement(session, check_record_stmt, {
#                     'VervotechId': record['VervotechId'],
#                     'ProviderHotelId': record['ProviderHotelId'],
#                     'ProviderFamily': record['ProviderFamily'],
#                 }).mappings().first()

#                 # Insert new record if it doesn't exist
#                 if not existing_record:
#                     execute_statement(session, insert_stmt, {
#                         'last_update': current_time,
#                         'VervotechId': record['VervotechId'],
#                         'UpdateDateFormat': record.get('UpdateDateFormat'),
#                         'ProviderHotelId': record['ProviderHotelId'],
#                         'ProviderFamily': record['ProviderFamily'],
#                         'ModifiedOn': current_time,
#                         'ChannelIds': record.get('ChannelIds'),
#                         'ProviderLocationCode': record.get('ProviderLocationCode')
#                     })
#                     update_status_stmt = text(update_status_stmt_template.format(table_name=table_name))
#                     execute_statement(session, update_status_stmt, {
#                         'VervotechId': record['VervotechId'],
#                         'ProviderHotelId': record['ProviderHotelId'],
#                         'ProviderFamily': record['ProviderFamily'],
#                         'status': 'Update data successful'
#                     })
#                     session.flush()  # Explicitly flush changes
#                     session.commit()  # Commit the transaction
#                     print(f"Inserting new record with VervotechId {record['VervotechId']}.")



#                 # Update existing record if any change is found
#                 elif (record['ProviderLocationCode'] != existing_record['ProviderLocationCode'] or
#                       record['ProviderHotelId'] != existing_record['ProviderHotelId'] or
#                       record['ProviderFamily'] != existing_record['ProviderFamily']):
#                     execute_statement(session, insert_stmt, {
#                         'last_update': current_time,
#                         'VervotechId': record['VervotechId'],
#                         'UpdateDateFormat': record.get('UpdateDateFormat'),
#                         'ProviderHotelId': record['ProviderHotelId'],
#                         'ProviderFamily': record['ProviderFamily'],
#                         'ModifiedOn': current_time,
#                         'ChannelIds': record.get('ChannelIds'),
#                         'ProviderLocationCode': record.get('ProviderLocationCode')
#                     })
#                     update_status_stmt = text(update_status_stmt_template.format(table_name=table_name))
#                     execute_statement(session, update_status_stmt, {
#                         'VervotechId': record['VervotechId'],
#                         'ProviderHotelId': record['ProviderHotelId'],
#                         'ProviderFamily': record['ProviderFamily'],
#                         'status': 'Update data successful'
#                     })
#                     session.flush()  # Explicitly flush changes
#                     session.commit()  # Commit the transaction
#                     print(f"Updating record with VervotechId {record['VervotechId']}.")




#                 # If nothing changed, mark as 'Skipping data'
#                 else:
#                     update_status_stmt = text(update_status_stmt_template.format(table_name=table_name))
#                     execute_statement(session, update_status_stmt, {
#                         'VervotechId': record['VervotechId'],
#                         'ProviderHotelId': record['ProviderHotelId'],
#                         'ProviderFamily': record['ProviderFamily'],
#                         'status': 'Skipping data'
#                     })
#                     session.flush()  # Explicitly flush changes
#                     session.commit()  # Commit the transaction
#                     print(f"Skipping unchanged record with VervotechId {record['VervotechId']}.")

#     # Process both tables
#     process_table_data('vervotech_hotel_map_new')
#     process_table_data('vervotech_hotel_map_update')




def update_vervotech_mapping_data(engine):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')

    def execute_statement(connection, statement, parameters=None):
        try:
            result = connection.execute(statement, parameters or {})
            connection.commit()  
            return result
        except exc.SQLAlchemyError as e:
            print(f"Error executing statement: {e}")
            connection.rollback() 
            raise

    insert_stmt = text("""
        INSERT INTO vervotech_mapping
        (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ModifiedOn, ChannelIds, ProviderLocationCode, status)
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId, :ProviderFamily, :ModifiedOn, :ChannelIds, :ProviderLocationCode, 'Update')
    """)

    check_record_stmt = text("""
        SELECT VervotechId, ProviderHotelId, ProviderFamily, ProviderLocationCode
        FROM vervotech_mapping
        WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId
    """)

    def update_table_status(connection, table_name, VervotechId, ProviderHotelId, status):
        update_status_stmt = text(f"""
            UPDATE {table_name}
            SET status = :status
            WHERE VervotechId = :VervotechId 
            AND ProviderHotelId = :ProviderHotelId 
        """)
        execute_statement(connection, update_status_stmt, {
            'VervotechId': VervotechId,
            'ProviderHotelId': ProviderHotelId,
            'status': status
        })

    def process_table_data(table_name):
        select_stmt = text(f"""
            SELECT * FROM {table_name}
            WHERE status = 'new_data'
        """)

        Session = sessionmaker(bind=engine)
        with Session() as connection:
            records = execute_statement(connection, select_stmt).mappings().all()
            if not records:
                print(f"No new records found in {table_name}.")
                return

            for record in records:
                existing_record = execute_statement(connection, check_record_stmt, {
                    'VervotechId': record['VervotechId'],
                    'ProviderHotelId': record['ProviderHotelId'],
                }).mappings().first()

                if existing_record:
                    update_table_status(connection, table_name, record['VervotechId'], record['ProviderHotelId'], 'Skipping data')
                    connection.flush()  
                    connection.commit()
                    print(f"Skipping......... unchanged record with VervotechId {record['VervotechId']}.")
                else:
                    execute_statement(connection, insert_stmt, {
                        'last_update': current_time,
                        'VervotechId': record['VervotechId'],
                        'UpdateDateFormat': record.get('UpdateDateFormat'),
                        'ProviderHotelId': record['ProviderHotelId'],
                        'ProviderFamily': record['ProviderFamily'],
                        'ModifiedOn': current_time,
                        'ChannelIds': record.get('ChannelIds'),
                        'ProviderLocationCode': record.get('ProviderLocationCode')
                    })
                    update_table_status(connection, table_name, record['VervotechId'], record['ProviderHotelId'], 'Update data successful')
                    connection.flush()  
                    connection.commit()
                    print(f"Inserting new record with VervotechId {record['VervotechId']}.")

    process_table_data('vervotech_hotel_map_new')
    process_table_data('vervotech_hotel_map_update')





def update_hotel_mapping_with_content(url, engine, table_name):
    """
    Updates all rows in the table where content_update_status is not 'Done'.
    For each row, it fetches the data from the API and updates the table with hotel details.
    """
    all_successful = True
    with engine.connect() as connection:
        try:
            select_query = text(f"""
                SELECT Id, ProviderHotelId, ProviderFamily
                FROM {table_name}
                WHERE (content_update_status IS NULL OR content_update_status != 'Done')
                AND ModifiedOn >= DATE_SUB(CURDATE(), INTERVAL 10 DAY)
            """)
            result = connection.execute(select_query)
            rows = result.fetchall() 

            if not rows:
                print("No records found where content_update_status is not 'Done'.")
                return  

            for row in rows:
                record_id, provider_hotel_id, provider_family = row 

                payload = get_content_by_provider_hotel_ids_create_payload(provider_hotel_id=provider_hotel_id, provider_family=provider_family)

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


def save_json_file(engine):
    """
    Fetches mapping data from the database and saves it as JSON files, with each file
    named after the `VervotechId`. If a file already exists for a particular `VervotechId`,
    the function appends new unique entries to avoid duplicates.
    """

    # Directory to save JSON files
    # json_dir = "/var/www/hotelmap.gtrsystem.com"
    json_dir = "D:/data_validation/logs/json_file"
    os.makedirs(json_dir, exist_ok=True)

    fetch_data_stmt = text("""
        SELECT VervotechId, ProviderHotelId, ProviderFamily, ProviderLocationCode
        FROM vervotech_mapping
    """)

    with engine.connect() as connection:
        records = connection.execute(fetch_data_stmt).fetchall()

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

            if os.path.exists(json_file_path):
                with open(json_file_path, 'r') as json_file:
                    existing_data = json.load(json_file)

                existing_set = {(entry['ProviderHotelId'], entry['ProviderFamily'], entry['ProviderLocationCode']) for entry in existing_data}

                new_entries = [
                    entry for entry in entries
                    if (entry['ProviderHotelId'], entry['ProviderFamily'], entry['ProviderLocationCode']) not in existing_set
                ]

                existing_data.extend(new_entries)
                entries = existing_data

            # Save the updated entries back to the JSON file
            with open(json_file_path, 'w') as json_file:
                json.dump(entries, json_file, indent=4)

            print(f"Saved data for VervotechId {vervotech_id} to {json_file_path}")


from database.db_connection import get_database_engine
from api_requests.fetch_data_from_database import get_provider_family_active_list, get_iit_supplier_code
from env_request.request_env import load_environment_variables_local


def update_with_provider_hotel_ids(url, payload, engine, table_name, record_id):
    """ 
    Fetches data from the API using the provided URL, payload, and headers, 
    and updates the specified database table with the hotel data using raw SQL queries.
    """
    with engine.connect() as connection:
        try:
            env_vars = load_environment_variables_local()
            api_key = env_vars['vervotech_api_key']
            headers = get_content_by_provider_hotel_ids_headers(api_key) 
            
            response = requests.post(url, headers=headers, data=payload)
            
            if response.status_code == 200:
                try:
                    data = response.json()
                except ValueError:
                    print(f"Failed to parse JSON for record {record_id}")
                    return False
                
                hotels = data.get('Hotels', [])
                
                for hotel in hotels:
                    provider_hotels = hotel.get('ProviderHotels', [])
                    for provider_hotel in provider_hotels:
                        # Extract required data
                        hotel_name = provider_hotel.get('Name')
                        family = provider_hotel.get('ProviderFamily')

                        env_vars = load_environment_variables_local()
                        engine = get_database_engine(env_vars=env_vars)
                        active_families = get_provider_family_active_list(table='vervotech_ProviderFamily', engine=engine)
                        # active_families = ['HotelBeds', 'EAN', 'MGHoliday', 'Agoda', 'DOTW', 'Restel']
                        iit_supplier_code = get_iit_supplier_code(table='vervotech_ProviderFamily', engine=engine)
                        # iit_supplier_code = ['hotelbeds', 'ean', 'mgholiday', 'agoda', 'DOTW', 'restel']
                        if family in active_families:
                            family_index = active_families.index(family)
                            family = iit_supplier_code[family_index]


                        city = provider_hotel.get('Contact', {}).get('Address', {}).get('City', 'Unknown')
                        country = provider_hotel.get('Contact', {}).get('Address', {}).get('Country', 'Unknown')

                        geo_code = provider_hotel.get('GeoCode', {})
                        lat = geo_code.get('Lat') if geo_code else None
                        long = geo_code.get('Long') if geo_code else None
                        country_code = provider_hotel.get('Contact', {}).get('Address', {}).get('CountryCode', 'Unknown')
                        last_update = datetime.now()
                        content_update_status = 'Done'

                        provider_hotel_id = provider_hotel.get('ProviderHotelId')
                        
                        # Save data to the database immediately
                        try:
                            update_query = text(f"""
                                UPDATE {table_name}
                                SET 
                                    ProviderFamily = :provider_family,
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

                            connection.execute(update_query, {
                                'provider_family': family,
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
                            connection.commit()
                            # print(f"Update successfully for provider hotel Id {provider_hotel_id}")
                        except exc.SQLAlchemyError as db_err:
                            print(f"Database error while updating provider hotel Id {provider_hotel_id}: {db_err}")
                            continue

                return True
            else:
                print(f"Failed to fetch data for record {record_id}. Status Code: {response.status_code}")
                return False
        
        except exc.SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            return False
        
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")
            return False


