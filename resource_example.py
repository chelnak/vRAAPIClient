#!/usr/bin/python
import getpass
import json
import sys
from time import sleep

from vraapiclient import vRAAPIConsumerClient

url = ''
usr = ''
passwd = getpass.getpass()

#Create a new consumer API client
client = vRAAPIConsumerClient(url, usr, passwd)

#requests.json file must exist and have valid JSON content
with open('templates/request.json') as f:
    payload = json.load(f)

#Submit new request. requestResource returns the request id
request = client.requestResource(payload)

#Monitor request progress and break from loop when no longer IN_PROGRESS
while True:
    sleep(10)

    requestState = client.getRequest(request)
    print requestState['state']
    if requestState['state'] != "IN_PROGRESS":
        break

#Extra logic to determine the result of the request
if requestState['state'] != "SUCCESSFUL":
    exit(requestState)

#End goal here is to return networking info of the new vm so we can grab the IP and run any
#extra tasks etc
resourceId = client.getResourceId(request)
resourceNetworking = client.getResourceNetworking(resourceId)
print resourceNetworking
