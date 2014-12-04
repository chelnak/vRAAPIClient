#!/usr/bin/python
from vraapiclient import vRAAPIConsumerClient
import json
from time import sleep
import sys

url = "vra.org.com"
usr = "user"
passwd = "password"

#Create a new consumer API client
client = vRAAPIConsumerClient(url, usr, passwd)

#requests.json file must exist and have valid JSON content
with open('request.json') as f:
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
