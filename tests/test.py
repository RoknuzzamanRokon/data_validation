def update_vervotech_mapping_data(engine):
    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')

    insert_into_table_3_stmt = text(f"""
        INSERT INTO vervotech_mapping
        (last_update, VervotechId, UpdateDateFormat, ProviderHotelId, ProviderFamily, ModifiedOn, ChannelIds, ProviderLocationCode, status)
        VALUES (:last_update, :VervotechId, :UpdateDateFormat, :ProviderHotelId, :ProviderFamily, :ModifiedOn, :ChannelIds, :ProviderLocationCode, 'Update')
    """)

    check_existing_record_stmt = text(f"""
        SELECT ProviderLocationCode FROM vervotech_mapping
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
            WHERE VervotechId = :VervotechId 
            AND ProviderHotelId = :ProviderHotelId 
            AND ProviderFamily = :ProviderFamily 
            AND (ProviderLocationCode = :ProviderLocationCode OR ProviderLocationCode IS NULL)
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
                    existing_record = connection.execute(check_existing_record_stmt, {
                        'VervotechId': record['VervotechId'],
                        'ProviderHotelId': record['ProviderHotelId'],
                        'ProviderFamily': record['ProviderFamily'],
                    }).fetchone()

                    if existing_record:
                        existing_location_code = existing_record['ProviderLocationCode']
                        incoming_location_code = record['ProviderLocationCode']

                        if existing_location_code == incoming_location_code:
                            print(f"Record with VervotechId {record['VervotechId']} and ProviderHotelId {record['ProviderHotelId']} already exists in vervotech_mapping. Skipping.")
                            connection.execute(update_status_skipping_stmt, {
                                'VervotechId': record['VervotechId'],
                                'ProviderHotelId': record['ProviderHotelId'],
                                'ProviderFamily': record['ProviderFamily'],
                                'ProviderLocationCode': incoming_location_code or None,
                            })
                            print(f"Updated status to 'Skipping data' in table {table_name} for VervotechId {record['VervotechId']}.")
                        else:
                            # If ProviderLocationCode is different, insert the new data
                            connection.execute(insert_into_table_3_stmt, {
                                'last_update': current_time,
                                'VervotechId': record['VervotechId'],
                                'UpdateDateFormat': record['UpdateDateFormat'] or None,
                                'ProviderHotelId': record['ProviderHotelId'],
                                'ProviderFamily': record['ProviderFamily'],
                                'ModifiedOn': current_time,
                                'ChannelIds': record['ChannelIds'] or None,
                                'ProviderLocationCode': incoming_location_code or None,
                            })
                            print(f"Inserted record with VervotechId {record['VervotechId']} into vervotech_mapping (status: 'Update').")

                            # Update the source table status to 'Update data successful'
                            connection.execute(update_status_successful_stmt, {
                                'VervotechId': record['VervotechId'],
                                'ProviderHotelId': record['ProviderHotelId'],
                                'ProviderFamily': record['ProviderFamily'],
                            })
                            print(f"Updated status to 'Update data successful' in table {table_name} for VervotechId {record['VervotechId']}.")
                    else:
                        # Insert if the record does not exist
                        connection.execute(insert_into_table_3_stmt, {
                            'last_update': current_time,
                            'VervotechId': record['VervotechId'],
                            'UpdateDateFormat': record['UpdateDateFormat'] or None,
                            'ProviderHotelId': record['ProviderHotelId'],
                            'ProviderFamily': record['ProviderFamily'],
                            'ModifiedOn': current_time,
                            'ChannelIds': record['ChannelIds'] or None,
                            'ProviderLocationCode': record['ProviderLocationCode'] or None,
                        })
                        print(f"Inserted record with VervotechId {record['VervotechId']} into vervotech_mapping (status: 'Update').")

                        # Update the source table status to 'Update data successful'
                        connection.execute(update_status_successful_stmt, {
                            'VervotechId': record['VervotechId'],
                            'ProviderHotelId': record['ProviderHotelId'],
                            'ProviderFamily': record['ProviderFamily'],
                        })
                        print(f"Updated status to 'Update data successful' in table {table_name} for VervotechId {record['VervotechId']}.")
            
            except exc.SQLAlchemyError as e:
                print(f"Error occurred during database operation: {e}")
                raise

    # Process updates from both tables
    update_mapping_from_table('vervotech_hotel_map_new')
    update_mapping_from_table('vervotech_hotel_map_update')
