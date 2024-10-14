from dotenv import load_dotenv
import os

# # Use raw string (r) to prevent escape sequence issues
# print(os.path.exists(r"D:\Company\InnovateSolution\var\.env_server"))  # Correct path


# # Fetch and print the values
# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASSWORD')
# db_host = os.getenv('DB_HOST')
# db_name = os.getenv('DB_NAME')
# vervotech_api_key = os.getenv('VERVOTECH_API_KEY')

# print("DB User:", db_user)
# print("DB Password:", db_password)
# print("DB Host:", db_host)
# print("DB Name:", db_name)
# print("Vervotech API Key:", vervotech_api_key)

def load_environment_variables_local():
    load_dotenv()
    env_vars = {
        'db_host': os.getenv('DB_HOST'),
        'db_user': os.getenv('DB_USER'),
        'db_password': os.getenv('DB_PASSWORD'),
        'db_name': os.getenv('DB_NAME'),
        'vervotech_api_key': os.getenv('VERVOTECH_API_KEY')
    }
    # print(env_vars) 
    return env_vars


def load_environment_variables():
    load_dotenv('/var/.env_server')
    return {
        'db_host': os.getenv('DB_HOST'),
        'db_user': os.getenv('DB_USER'),
        'db_password': os.getenv('DB_PASSWORD'),
        'db_name': os.getenv('DB_NAME'),
        'vervotech_api_key': os.getenv('API_KEY_VERVOTECH')
    }
