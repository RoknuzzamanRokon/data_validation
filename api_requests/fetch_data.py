import requests
import pandas as pd
from sqlalchemy import create_engine, text
import json
from datetime import datetime, timedelta, timezone


def save_data_to_db(data, engine, table_name):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
    insert_stmt = text(f"""
        INSERT INTO {table_name} (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ChannelIds, ProviderLocationCode)
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId,  :ProviderFamily, :ChannelIds, :ProviderLocationCode)
        ON DUPLICATE KEY UPDATE
            last_update = :last_update,
            VervotechId = :VervotechId,
            UpdateDateFormat = :UpdateDateFormat,
            ProviderHotelId = :ProviderHotelId,
            ProviderFamily = :ProviderFamily,
            ChannelIds = :ChannelIds,
            ProviderLocationCode = :ProviderLocationCode
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
                    'ProviderLocationCode': record.get('ProviderLocationCode') or None
                })
                print(f"Record with VervotechId {record.get('VervotechId')} inserted/updated successfully.")
            transaction.commit()
            print("-----------------------------------------------------------Transaction committed successfully.------------------------------------")
        except Exception as e:
            transaction.rollback()
            print(f"Transaction failed: {e}")


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




def insert_columns(connection_string, table_name):
    # Create connection engine
    engine = create_engine(connection_string)

    # List of columns to be added
    columns_to_add = [
        'Name', 'Latitude', 'Longitude', 'AddressLine1', 'AddressLine2', 'CityName', 'StateName', 
        'StateCode', 'CountryName', 'CountryCode', 'PostalCode', 'Rating', 'PropertyType', 
        'ChainName', 'ChainCode', 'BrandName', 'CityCode', 'CityLocationId', 'MasterCityName', 
        'LocationIds', 'Phones', 'Emails', 'Fax', 'Website', 'AirportCodes', 'TrainStations', 
        'ProviderHotelId', 'ProviderFamily', 'GooglePlusCode', 'GooglePlaceId', 'Tags'
    ]

    # Add each column to the table
    with engine.connect() as connection:
        for column in columns_to_add:
            try:
                alter_query = text(f"""
                ALTER TABLE {table_name}
                ADD COLUMN {column} VARCHAR(255);
                """)
                connection.execute(alter_query)
                print(f"Column '{column}' added.")
            except Exception as e:
                print(f"Error adding column '{column}': {str(e)}")

    print("Column insertion process completed.")






def update_mapping_fetch_data(url, params, headers, engine, table_name):
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            break

        try:
            response_data = response.json()
        except ValueError as e:
            print(f"JSON decode error: {e}")
            print(f"Response content: {response.text}")
            break

        if 'Mappings' in response_data and response_data['Mappings']:
            new_data = response_data['Mappings']
            if "ResumeKey" in response_data:
                save_data_to_db(new_data, engine, table_name)
                params['resumeKey'] = response_data["ResumeKey"]
            else:
                print("No more ResumeKey found. Fetching complete.")
                break
        else:
            print("No data found in response.")
            break


