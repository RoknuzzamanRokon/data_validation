from datetime import datetime, timedelta, timezone


def get_update_mapping_params(providerFamily):
    current_time = datetime.now(timezone.utc)
    previous_time = current_time - timedelta(days=1)
    formatted_previous_time = previous_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    params = {
            'limit': 500,
            'providerFamily': providerFamily,
            'lastUpdateDateTime': f"{formatted_previous_time}"
        }
    return params


def get_new_mapping_params(providerFamily):
    current_time = datetime.now(timezone.utc)
    previous_time = current_time - timedelta(days=1)
    formatted_previous_time = previous_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    params = {
            'limit': 500,
            'providerFamily': providerFamily,
            'lastUpdateDateTime': f"{formatted_previous_time}"
        }
    return params
