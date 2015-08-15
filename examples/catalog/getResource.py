#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

resourceId = '171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'

#Print table
client.getResource(id=resourceId)

#Get JSON Object
resource = client.getResource(id=resourceId, show='json')

#Print id and name
print resource['id']
print resource['name']

#Use json.dumps() to get json string
resourceJSONString = json.dumps(resource)
print resourceJSONString
