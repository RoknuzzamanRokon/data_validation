from api_call.params import get_update_mapping_params
from api_call.urls import get_update_mapping_url
from api_call.headers import get_update_mapping_headers
from env_request.request_env import load_environment_variables,load_environment_variables_local
from database.db_connection import get_database_engine
from api_requests.log_runner import log_run_time_update_mapping_local
from api_requests.fetch_data_from_api import update_mapping_fetch_data


def get_update_mapping_data_process():
    # env_vars = load_environment_variables()
    env_vars = load_environment_variables_local()

    # print(env_vars['db_user'])
    engine = get_database_engine(env_vars)
    # print(engine)
    table_name = "vervotech_hotel_map_update"

    url = get_update_mapping_url()
    # print(url)
    params = get_update_mapping_params()
    # print(params)

    headers = get_update_mapping_headers(env_vars['vervotech_api_key'])
    # print(headers)
    log_run_time_update_mapping_local(execution_date=params['lastUpdateDateTime'])
    log = update_mapping_fetch_data(url, params, headers, engine, table_name)
    # print(log)
    print("Fetching and saving process completed.")



# def get_update_mapping_data_process():
#     # Load local environment variables
#     env_vars = load_environment_variables_local()

#     # Debug: print out all environment variables to confirm
#     print("Database User:", env_vars['db_user'])
#     print("Database Password:", env_vars['db_password'])
#     print("Database Host:", env_vars['db_host'])
#     print("Database Name:", env_vars['db_name'])

#     # Check the engine creation process
#     engine = get_database_engine(env_vars)
#     print(engine)

#     table_name = "vervotech_hotel_map_update"

#     # API processing
#     url = get_update_mapping_url()
#     print("API URL:", url)
    
#     params = get_update_mapping_params()
#     print("API Params:", params)

#     headers = get_update_mapping_headers(env_vars['vervotech_api_key'])
#     print("API Headers:", headers)
    
#     # Log and fetch data
#     log_run_time_update_mapping_local(execution_date=params['lastUpdateDateTime'])
#     log = update_mapping_fetch_data(url, params, headers, engine, table_name)
#     print(log)
#     print("Fetching and saving process completed.")