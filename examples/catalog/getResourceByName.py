#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

resourceName = 'dev-svr-02'

#Print table
client.getResourceByName(name=resourceName, show='table')

#Get JSON Object
resource = client.getResourceByName(name=resourceName)

#Print id and name
print resource['id']
print resource['name']

#Use json.dumps() to get json strong
resourceJSONString = json.dumps(resource)
print resourceJSONString
