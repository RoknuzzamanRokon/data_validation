response = requests.post(url, headers=headers, data=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON content
    data = response.json()
    
    # Extract and print specific details about the hotel
    hotels = data.get('Hotels', [])
    
    for hotel in hotels:
        provider_hotels = hotel.get('ProviderHotels', [])
        
        for provider_hotel in provider_hotels:
            hotel_name = provider_hotel.get('Name')
            provider_hotel_id = provider_hotel.get('ProviderHotelId')
            country = provider_hotel.get('Contact', {}).get('Address', {}).get('Country')
            city = provider_hotel.get('Contact', {}).get('Address', {}).get('City')
            address_line1 = provider_hotel.get('Contact', {}).get('Address', {}).get('Line1')
            postal_code = provider_hotel.get('Contact', {}).get('Address', {}).get('PostalCode')
            latitude = provider_hotel.get('GeoCode', {}).get('Lat')
            longitude = provider_hotel.get('GeoCode', {}).get('Long')
            facilities = provider_hotel.get('Facilities', [])

            # Print the extracted information
            print(f"Hotel Name: {hotel_name}")
            print(f"Provider Hotel ID: {provider_hotel_id}")
            print(f"Location: {address_line1}, {city}, {country}, Postal Code: {postal_code}")
            print(f"Geocode: Latitude {latitude}, Longitude {longitude}")
            
            # Print facilities
            print("Facilities:")
            for facility in facilities:
                facility_name = facility.get('Name')
                group_name = facility.get('GroupName')
                print(f"- {facility_name} ({group_name})")
            print("\n")  # For better readability
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
