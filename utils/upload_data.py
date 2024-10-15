import pandas as pd
from sqlalchemy import create_engine
import pymysql


db_host = "ls-2606b703826b2a67a9b8ffc6a904a205faee891e.c1m8so4gsag3.ap-southeast-1.rds.amazonaws.com"
db_user = "itt_contents"
db_password = "h%40HMbaa98569745"
db_name = "itt_master_contents"
table_name = "vervotech_hotel_list"

connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(connection_string)

csv_file_path = "D:/Company/InnovateSolution/csv01_02102024/Vervotech-Mapping-2024-09-21/gtrs_hotels_a5a093d7-a4f5-4063-9b4c-38facb3084d8.csv"
df = pd.read_csv(csv_file_path, low_memory=False)



df['VervotechId'] = df['UnicaId']  
df['last_update'] = pd.NA  
df['UpdateDateFormat'] = pd.NA

columns_to_insert = ['VervotechId',  'Name', 'Latitude', 'Longitude', 'AddressLine1', 'AddressLine2', 'CityName', 'StateName', 
    'StateCode', 'CountryName', 'CountryCode', 'PostalCode', 'Rating', 'PropertyType', 
    'ChainName', 'ChainCode', 'BrandName', 'CityCode', 'CityLocationId', 'MasterCityName', 
    'LocationIds', 'Phones', 'Emails', 'Fax', 'Website', 'AirportCodes', 'TrainStations', 
    'ProviderHotelId', 'ProviderFamily', 'GooglePlusCode', 'GooglePlaceId', 'Tags'
]

try:
    for i, row in df[columns_to_insert].iterrows():
        single_row_df = pd.DataFrame([row])

        single_row_df.to_sql(table_name, con=engine, if_exists='append', index=False)

        print(f"Upload successful: {i + 1} row(s) inserted.")
    print("Upload successfully complete.")

except Exception as e:
    print(f"An error occurred: {e}")


