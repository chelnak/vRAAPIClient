#!/usr/bin/python
import getpass
import json
import os

from globalconfig import passwd, url, usr
from time import sleep
from sys import exit
from vraapiclient import catalog

#Get the current directory
currentDirectory = os.path.dirname(os.path.abspath(__file__))

client = catalog.ConsumerClient(url, usr, passwd)

#Create the JSON payload for the Post and submit the request
with open('requestFormatted.json') as f:
    payload = json.load(f)

requestId = client.requestResource(payload)

print "Request submitted: {id}".format(id=requestId)

acceptedStates = ['FAILED', 'SUCCESSFUL']

#Wait for the request to finish
print "Waiting for the request to complete..."

while True:
    request = client.getRequest(requestId)
    requestState = request['state']

    if requestState in acceptedStates:
        if requestState != 'SUCCESSFUL':
            exit(request)
        else:
            print "Request successful"
            break

    sleep(2)

#Return networking information for the new resource
resource = client.getRequestResource(requestId)
#Grab the id here.
#We know we have only requested a single resource so we can specify and index of 0
resourceId = resource[0]['id']
resourceNetworking = client.getResourceNetworking(resourceId)

for i in resourceNetworking:
    print "{key} : {value}".format(key=i['key'], value=i['value']['value'])
