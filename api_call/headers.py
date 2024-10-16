def get_update_mapping_headers(api_key):
    return {
        'accountId': 'gtrs',
        'syncId': '323',
        'apikey': api_key
    }


def get_new_mapping_headers(api_key):
    return {
        'accountId': 'gtrs',
        'syncId': '323',
        'apikey': api_key
    }


def get_content_by_provider_hotel_ids_headers(api_key):
    return {
        'accountid': 'gtrs',
        'apikey': api_key,
        'Content-Type': 'application/json'
    }