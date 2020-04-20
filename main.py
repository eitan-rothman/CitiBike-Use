import json
import urllib.request
from bs4 import BeautifulSoup
import pymongo

def getSystem():
    system_url = urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/system_information.json")
    system_data= json.loads(system_url.read().decode())
    final_system = system_data['data']['stations']
    print(final_system)

def getStatus():
    status_url = urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_status.json")
    status_data = json.loads(status_url.read().decode())
    final_status = status_data['data']['stations']
    print(final_status)

def main():
    getSystem()
    getStatus()


	# connect to NoSQL DB
    myclient = pymongo.MongoClient("******")
	mydb = myclient["CitiBikeUsage"]
	
	mycol = mydb["SystemStaus"] #insert infor for System
	x = mycol.insert_many(final_system) 

	mycol = mydb["StatusData"] #insert infor for status
	x = mycol.insert_many(final_status) 

main()
