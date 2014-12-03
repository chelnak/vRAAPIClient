vRAAPIClient
============

A python wrapper for the vRealize Automation REST API

Created for two reasons:
1 - because
2 - Couldn't get cloudclient to do certain things and the API is more flexible

Returns API responses in JSON format

usage:

from vraapiclient import vRAAPIClient

url = "vra host"
usr = "user"
pass = "pass"

client = vRAAPIClient(url, usr, passwd)

resources = client.getAllResources()

vmNetwork = client.getResourceNetworking("1b045274-f5de-4233-b800-e760fb3de4e2")

print vmNetwork


TODO
- Lots
