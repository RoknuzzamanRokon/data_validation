from sqlalchemy import create_engine
import os


def get_database_engine(env_vars):
    return create_engine(f"mysql+pymysql://{env_vars['db_user']}:{env_vars['db_password']}@{env_vars['db_host']}/{env_vars['db_name']}")


def get_vervotech_api_key(vervotech_api):
    return f"{vervotech_api['vervotech_api_key']}"