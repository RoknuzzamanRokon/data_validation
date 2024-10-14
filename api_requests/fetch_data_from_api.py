import requests
import json
from datetime import datetime, timedelta, timezone
from sqlalchemy import create_engine, Table, MetaData, text

def save_data_to_db(data, engine, table_name):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
    log = ""
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
                log += f"Record with VervotechId {record.get('VervotechId')} inserted/updated successfully.\n"
            transaction.commit()
            log += "Transaction committed successfully.\n"
        except Exception as e:
            transaction.rollback()
            log += f"Transaction failed: {e}\n"
    return log

def update_mapping_fetch_data(url, params, headers, engine, table_name):
    log = ""
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            log += f"Error: Received status code {response.status_code}\n"
            log += f"Response: {response.text}\n"
            break

        try:
            response_data = response.json()
        except ValueError as e:
            log += f"JSON decode error: {e}\n"
            log += f"Response content: {response.text}\n"
            break

        if 'Mappings' in response_data and response_data['Mappings']:
            new_data = response_data['Mappings']
            log += save_data_to_db(new_data, engine, table_name)
            if "ResumeKey" in response_data:
                params['resumeKey'] = response_data["ResumeKey"]
            else:
                log += "No more ResumeKey found. Fetching complete.\n"
                break
        else:
            log += "No data found in response.\n"
            break
    return log
