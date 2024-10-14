import sys
import json
import mysql.connector
import numpy
from datetime import datetime
import bson.json_util as json_util
import requests
import os

# Database connection
mydb = mysql.connector.connect(
    host="ls-f53587e703f0847e5a2ceb45eaf2921bd1089f28.c1m8so4gsag3.ap-southeast-1.rds.amazonaws.com",
    user="vervotech",
    password="XvB32JVY6SZjFjBS2QV5hN",
    database="vervotech_db"
)
mycursor = mydb.cursor(dictionary=True)

# SQL query
sql = "SELECT VervotechId, ProviderHotelId, ProviderFamily FROM vervotech_mapping_hotel_id WHERE ProviderFamily = 'ean' Order By Id ASC"
mycursor.execute(sql)
Vervotech_result = mycursor.fetchall()

# Define master path
master_path = "/var/www/hoteljson.gtrsystem.com/"

# Initialize hotel mapping array
hotel_mapping_array = []

# Read data
for v_data in Vervotech_result:
    for provider_data in Vervotech_result:
        if v_data['VervotechId'] == provider_data['VervotechId']:
            VervotechId = provider_data['VervotechId']
            ProviderHotelId = provider_data['ProviderHotelId']
            ProviderFamily = provider_data['ProviderFamily']
            print(VervotechId)
            print(ProviderHotelId)
            print(ProviderFamily)
            
            # Create directory if it doesn't exist
            path_d = os.path.join(master_path, ProviderFamily)
            if not os.path.exists(path_d):
                os.makedirs(path_d, mode=0o777)
            
            hotel_mapping_array.append(provider_data)
    
    # Generate file name and path
    VervotechId_file_name = "%s.json" % VervotechId
    VervotechId_file_generate_path = os.path.join(path_d, VervotechId_file_name)
    
    # Write JSON data to file
    with open(VervotechId_file_generate_path, "w") as loc_outfile:
        loc_outfile.write(json_util.dumps(hotel_mapping_array))
    
    # Clear the array for the next iteration
    hotel_mapping_array.clear()
