import urllib.request, json 
import pymongo

with urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_status.json") as url:
    rawData = json.loads(url.read().decode())
    data = rawData['data']['stations']
    print(data)
    
    
#def database():
    #take the data above and 
    
  