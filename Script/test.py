import urllib, json

url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data