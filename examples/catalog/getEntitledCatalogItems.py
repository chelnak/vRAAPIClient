#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import catalog

client = catalog.ConsumerClient(url, usr, passwd)

#Print table
client.getEntitledCatalogItems()

#Get JSON Object
entitledCatalogItems = client.getEntitledCatalogItems(show='json')

#Loop through object and print id and name
for i in entitledCatalogItems:

	print i['catalogItem']['id']
	print i['catalogItem']['name']

#Use json.dumps() to get json string
entitledCatalogItemsJSONString = json.dumps(entitledCatalogItems)
print entitledCatalogItemsJSONString
