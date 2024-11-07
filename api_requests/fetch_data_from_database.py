import pandas as pd


def get_provider_family_active_list(table, engine):
    query = f"SELECT ProviderFamily FROM {table} WHERE status = 'active'"
    df = pd.read_sql(query, engine)

    provider_family_active_list = provider_families = df['ProviderFamily'].tolist()
    return provider_family_active_list