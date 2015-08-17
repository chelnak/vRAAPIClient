#!/usr/bin/python
import getpass
import json
import os

from jinja2 import Environment, FileSystemLoader
from time import sleep
from sys import exit
from globalconfig import passwd, url, usr
from vraapiclient import catalog

#Get the current directory
currentDirectory = os.path.dirname(os.path.abspath(__file__))

client = catalog.ConsumerClient(url, usr, passwd)

#Set up jinja2 environment
env = Environment(loader=FileSystemLoader(currentDirectory))
template = env.get_template('requestFormatted.json')

#Set all configurable parameters here
params = {}

#Create the JSON payload for the Post
#This is where params are added to the json payload

payload = json.loads(template.render(params=params))

#Submit request
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
#We know we have only requested a single resource so we can specify and index of 0
resourceId = resource[0]['id']
resourceNetworking = client.getResourceNetworking(resourceId)

for i in resourceNetworking:
    print "{key} : {value}".format(key=i['key'], value=i['value']['value'])
