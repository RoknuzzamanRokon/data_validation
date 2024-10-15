import os
from datetime import datetime

def log_run_time_update_mapping_local(execution_date):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%I:%M %p %m/%d/%Y")

    # log_directory = '/var/www/VerVotech-Contents-Mapping/data_validation/logs'
    log_directory = 'D:/data_validation/logs'
    log_file_path = os.path.join(log_directory, 'update_mapping_date_runTime.txt')

    # Check if the directory exists, if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        print(f"Directory {log_directory} created.")

    # Write log data
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Running date:- {formatted_time} collect data from: {execution_date} time.\n")
    print(f"Log written to {log_file_path}")


def log_run_time_new_mapping_local(execution_date):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%I:%M %p %m/%d/%Y")

    # log_directory = '/var/www/VerVotech-Contents-Mapping/data_validation/logs'
    log_directory = 'D:/data_validation/logs'

    log_file_path = os.path.join(log_directory, 'new_mapping_date_runTime.txt')

    # Check if the directory exists, if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        print(f"Directory {log_directory} created.")

    # Write log data
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Running date:- {formatted_time} collect data from: {execution_date} time.\n")
    print(f"Log written to {log_file_path}")



# def log_run_time_update_mapping_server(execution_date):
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%I:%M %p %m/%d/%Y")
#     log_file_path = os.path.join('/var/www/VerVotech-Contents-Mapping/logFile', 'update_mapping_date_scheduler_runTime.txt')
#     with open(log_file_path, 'a') as log_file:
#         log_file.write(f"Running date:- {formatted_time} collect data from: {execution_date} time.\n")
