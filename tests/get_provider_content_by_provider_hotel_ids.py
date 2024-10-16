import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

vervotech_api_key = os.getenv('VERVOTECH_API_KEY')

url = "https://hotelmapping.vervotech.com/api/3.0/content/GetProviderContentByProviderHotelIds"

payload = json.dumps({
  "ProviderHotelIdentifiers": [
    {
      "ProviderHotelId": "1000000",
      "ProviderFamily": "Agoda"
    }
  ]
})
headers = {
  'accountid': 'gtrs',
  'apikey': f'{vervotech_api_key}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

if response.status_code == 200:
    data = response.json()

    hotels = data.get('Hotels', [])

    # print(hotels)

    for hotel in hotels:
        provider_hotels = hotel.get('ProviderHotels', [])

        # print(provider_hotels)
        for provider_hotel in provider_hotels:
            hotel_name = provider_hotel.get('Name')
            print(f"hotel_name: {hotel_name}")

            city = provider_hotel.get('Contact', {}).get('Address',{}).get('City')
            print(f"hotel_city: {city}")
            country = provider_hotel.get('Contact', {}).get('Address',{}).get('Country')
            print(f"hotel_country: {country}")
            countryCode = provider_hotel.get('Contact', {}).get('Address',{}).get('CountryCode')
            print(f"country_code: {countryCode}")
            lat = provider_hotel.get('GeoCode', {}).get('Lat')
            print(f"hotel_latitude: {lat}")
            long = provider_hotel.get('GeoCode', {}).get('Long')
            print(f"hotel_longitude: {long}")


