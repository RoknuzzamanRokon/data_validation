import pandas as pd


def get_provider_family_active_list(table, engine):
    query = f"SELECT ProviderFamily FROM {table} WHERE status = 'active'"
    df = pd.read_sql(query, engine)

    provider_family_active_list = df['ProviderFamily'].tolist()
    return provider_family_active_list
    

def get_iit_supplier_code(table, engine):
    query = f"SELECT iit_supplier_code FROM {table} WHERE status = 'active'"
    df = pd.read_sql(query, engine)

    iit_supplier_code = df['iit_supplier_code'].tolist()
    return iit_supplier_code