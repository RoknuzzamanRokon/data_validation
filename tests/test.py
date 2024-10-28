import requests

url = "https://hotelmapping.vervotech.com/api/3.0/mappings/GetUpdatedMappings?limit=1000&lastUpdateDateTime=2024-10-16T06:51:27Z"


headers = {
  'accountId': 'gtrs',
  'syncId': '323',
  'apikey': 'b0ae90d7-2507-4751-ba4d-d119827c1ed2'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
