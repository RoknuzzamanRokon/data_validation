import os
from dotenv import load_dotenv
import sqlalchemy as db
from sqlalchemy import text, exc
from payload.payload_generator import create_payload

def update_hotel_mapping(url, headers, engine, table_name):
    """
    Updates all rows in the table where content_status is not 'Done'.
    For each row, it fetches the data from the API and updates the table with hotel details.
    
    Args:
        url (str): The API URL.
        headers (dict): The headers required for the API request.
        engine (SQLAlchemy engine): The SQLAlchemy engine object connected to the database.
        table_name (str): The name of the table to update in the database.
    """
    # Open a new database connection using the engine
    with engine.connect() as connection:
        try:
            # Select rows where content_status is not 'Done'
            select_query = text(f"SELECT Id, ProviderHotelId, ProviderFamily FROM {table_name} WHERE content_status != 'Done'")
            result = connection.execute(select_query)
            
            # Iterate over each row
            for row in result:
                provider_hotel_id = row['ProviderHotelId']
                provider_family = row['ProviderFamily']
                record_id = row['Id']
                
                # Generate payload dynamically
                payload = create_payload(provider_hotel_id, provider_family)

                # Call the API and update the row in the database
                update_with_provider_hotel_ids(url, payload, headers, engine, table_name, record_id)
        
        except exc.SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
        
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")

def update_with_provider_hotel_ids(url, payload, headers, engine, table_name, record_id):
    """
    Fetches data from the API using the provided URL, payload, and headers, 
    and updates the specified database row with the hotel data using raw SQL queries.

    Args:
        url (str): The API URL.
        payload (str): The JSON payload for the API request.
        headers (dict): The headers required for the API request.
        engine (SQLAlchemy engine): The SQLAlchemy engine object connected to the database.
        table_name (str): The name of the table to update in the database.
        record_id (int): The record ID to update in the database.
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
                            'record_id': record_id
                        })
            else:
                print(f"Failed to fetch data for record {record_id}. Status Code: {response.status_code}")
        
        except exc.SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
        
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")

