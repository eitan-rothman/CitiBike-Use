import urllib.request, json 

with urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_status.json") as url:
    data = json.loads(url.read().decode())
    print(data)