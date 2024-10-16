from dotenv import load_dotenv
import os


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
    env_vars = {
        'db_host': os.getenv('DB_HOST'),
        'db_user': os.getenv('DB_USER'),
        'db_password': os.getenv('DB_PASSWORD'),
        'db_name': os.getenv('DB_NAME'),
        'vervotech_api_key': os.getenv('VERVOTECH_API_KEY')
    }
    # print(env_vars) 
    return env_vars
