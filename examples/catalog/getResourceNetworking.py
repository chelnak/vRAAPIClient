#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

resourceId='171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'

#Get JSON Object
resource = client.getResource(id=resourceId)

#Print id and name
print resource['id']
print resource['name']

#Use json.dumps() to get raw json
resourceRaw = json.dumps(resource)
print resourceRaw
