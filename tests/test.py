from sqlalchemy import text
from datetime import datetime

def update_vervotech_mapping(engine):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
    log = ""

    # Define the insert statement for table 3 (vervotech_mapping)
    insert_into_table_3_stmt = text(f"""
        INSERT INTO vervotech_mapping
        (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ModifiedOn, ChannelIds, ProviderLocationCode, status)
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId, :ProviderFamily, :ModifiedOn, :ChannelIds, :ProviderLocationCode, 'update')
    """)

    # Define the update status statement for tables 1 and 2
    update_status_stmt = text(f"""
        UPDATE {{}}
        SET status = 'update successful'
        WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId
    """)

    # Check if record exists in table 3 (vervotech_mapping)
    check_existing_record_stmt = text(f"""
        SELECT COUNT(*) FROM vervotech_mapping
        WHERE VervotechId = :VervotechId AND ProviderHotelId = :ProviderHotelId
    """)

    def update_mapping_from_table(table_name):
        # Fetch records from table 1 or 2 where status is "new_data"
        select_new_data_stmt = text(f"""
            SELECT * FROM {table_name}
            WHERE status = 'new_data'
        """)
        with engine.connect() as connection:
            records = connection.execute(select_new_data_stmt).fetchall()

            for record in records:
                # Check if record already exists in table 3
                result = connection.execute(check_existing_record_stmt, {
                    'VervotechId': record['VervotechId'],
                    'ProviderHotelId': record['ProviderHotelId']
                }).scalar()

                if result > 0:
                    log += f"Record with VervotechId {record['VervotechId']} and ProviderHotelId {record['ProviderHotelId']} already exists in vervotech_mapping. Skipping.\n"
                else:
                    # If not exists, insert into table 3 (vervotech_mapping)
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
                    log += f"Inserted record with VervotechId {record['VervotechId']} into vervotech_mapping.\n"

                    # Update the status of the record in table 1 or 2
                    connection.execute(update_status_stmt.format(table_name), {
                        'VervotechId': record['VervotechId'],
                        'ProviderHotelId': record['ProviderHotelId']
                    })
                    log += f"Updated status to 'update successful' in table {table_name} for VervotechId {record['VervotechId']}.\n"

    # Update from both vervotech_hotel_map_new (table 1) and vervotech_hotel_map_update (table 2)
    update_mapping_from_table('vervotech_hotel_map_new')
    update_mapping_from_table('vervotech_hotel_map_update')

    return log
