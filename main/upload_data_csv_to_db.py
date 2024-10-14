import pymysql
from request_env.request_env import get_db_credentials
from api_requests.fetch_data import fetch_and_process_data

# Get database credentials
db_creds = get_db_credentials()

# Set up connection string and table name
table_name = "vervotech_hotel_list"
connection_string = f"mysql+pymysql://{db_creds['db_user']}:{db_creds['db_password']}@{db_creds['db_host']}/{db_creds['db_name']}"

# Set up CSV file path
csv_file_path = "/var/www/VerVotech-Contents-Mapping/Vervotech-Mapping-2024-09-21/gtrs_hotels_a5a093d7-a4f5-4063-9b4c-38facb3084d8.csv"

# Fetch and process data
fetch_and_process_data(csv_file_path, connection_string, table_name)