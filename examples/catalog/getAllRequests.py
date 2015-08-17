#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

#Print table
client.getAllRequests()

#Get JSON Object
requestsJSONObject = client.getAllRequests(show='json')

#Loop through object and print name
for i in requestsJSONObject:
    print i['name']

#Use json.dumps() to get json string
requestsJSONString = json.dumps(requestsJSONObject)
print requestsJSONString
