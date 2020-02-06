import json
import urllib.request
from bs4 import BeautifulSoup

def getSystem():
    system_url = urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/system_information.json")
    system_data= json.loads(system_url.read().decode())
    print(system_data)

def getStatus():
    status_url = urllib.request.urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_status.json")
    status_data = json.loads(status_url.read().decode())
    print(status_data)

def parse():


def main():

main()