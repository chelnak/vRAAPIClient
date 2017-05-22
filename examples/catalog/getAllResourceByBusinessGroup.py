#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

#update your business group here
business_group = 'devops_test'

#Print table
client.getResourceByBusinessGroup(name=business_group, show='table')

#Get JSON Object
resource = client.getResourceByBusinessGroup(name=business_group, limit='1000' )

#Print id and name
for item in resource['content']:
    print item['id']
    print item['name']

#Use json.dumps() to get json strong
resourceJSONString = json.dumps(resource, sort_keys=True, indent=4)
print resourceJSONString
