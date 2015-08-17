#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

resourceName = 'ITS-SP-161'

#Print table
client.getResourceByName(name=resourceName, show='table')

#Get JSON Object
resource = client.getResourceByName(name=resourceName)

#Print id and name
print resource['id']
print resource['name']

#Use json.dumps() to get raw json
resourceRaw = json.dumps(resource)
print resourceRaw
