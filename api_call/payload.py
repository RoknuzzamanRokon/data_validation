import json

def get_content_by_provider_hotel_ids_create_payload(provider_hotel_id, provider_family):
    """
    Creates a JSON payload for the API request.
    
    Args:
        provider_hotel_id (str): The ProviderHotelId to be included in the payload.
        provider_family (str): The ProviderFamily to be included in the payload.
    
    Returns:
        str: The JSON string payload for the API request.
    """
    payload = {
        "ProviderHotelIdentifiers": [
            {
                "ProviderHotelId": provider_hotel_id,
                "ProviderFamily": provider_family
            }
        ]
    }
    return json.dumps(payload)
