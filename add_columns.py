from sqlalchemy import create_engine, text
import pymysql

# Database connection details
db_host = "ls-2606b703826b2a67a9b8ffc6a904a205faee891e.c1m8so4gsag3.ap-southeast-1.rds.amazonaws.com"
db_user = "itt_contents"
db_password = "h%40HMbaa98569745"
db_name = "itt_master_contents"
table_name = "vervotech_hotel_list"

# Create connection engine
connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
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
        alter_query = text(f"""
        ALTER TABLE {table_name}
        ADD COLUMN {column} VARCHAR(255);
        """)
        connection.execute(alter_query)
        print(f"Column '{column}' added.")
