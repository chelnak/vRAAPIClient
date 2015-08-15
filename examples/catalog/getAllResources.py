#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

#Print table
client.getAllResources()

#Get JSON Object
resourcesJSONObject = client.getAllResources(show='json')

#Loop through object and print name
for i in resourcesJSONObject:
    print i['name']

#Use json.dumps() to get json string
resourcesJSONString = json.dumps(resourcesJSONObject)
print resourcesJSONString
