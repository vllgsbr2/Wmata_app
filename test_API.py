########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'api_key': 'f19a156811e749d690033de5800b0c4f',
}

params = urllib.parse.urlencode({
    # Request parameters
    'LineCode': 'YL',
})

conn = http.client.HTTPSConnection('api.wmata.com')
conn.request("GET", "/Rail.svc/json/jStations?%s" % params, "{body}", headers)
response = conn.getresponse()
json_str = response.read()
root_dict     = json.loads(json_str)
conn.close()

# print(dict.keys())
#
# for i in dict['Stations']:
#     # print(i.keys())
#     print(i)
#     break

# dict with 1 entry called stations with a list of 27 stations
# each station has
# Code
# Name
# StationTogether1
# StationTogether2
# LineCode1
# LineCode2
# LineCode3
# LineCode4
# Lat
# Lon
# Address

# {'Code': 'B08', 'Name': 'Silver Spring', 'StationTogether1': '', 'StationTogether2':
#  '', 'LineCode1': 'RD', 'LineCode2': None, 'LineCode3': None, 'LineCode4': None,
#  'Lat': 38.993841, 'Lon': -77.031321, 'Address': {'Street': '8400 Colesville Road',
#  'City': 'Silver Spring', 'State': 'MD', 'Zip': '20910'}}

#iterate through stations
for secondary_dict, stations in root_dict.items():
    for station in stations:
        print(station['Name'], station['Code'])
