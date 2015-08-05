#!/usr/bin/python
import getpass
import json
import os

from globalconfig import passwd, url, usr
from vraapiclient import catalog

#Get the current directory
currentDirectory = os.path.dirname(os.path.abspath(__file__))

client = catalog.ConsumerClient(url, usr, passwd)

#Create the JSON payload for the Post
with open('requestFormatted.json') as f:
	payload = json.load(f)

request = client.requestResource(payload)

print "Request submitted: {id}".format(id=request)
