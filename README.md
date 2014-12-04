vRAAPIClient
============

A python wrapper for the vRealize Automation REST API

Created for two reasons:
1 - because
2 - Couldn't get cloudclient to do certain things and the API is more flexible

Returns API responses in JSON format

Dependencies:
===========
- Coming soon!

Basic usage:
============

from vraapiclient import vRAAPIClient

url = "vra host"
usr = "user"
pass = "pass"

client = vRAAPIClient(url, usr, passwd)

resources = client.getAllResources()

print resources

example.py:
==========
- chmod +x example.py
- ./example.py
- You must create a file containing the request data in JSON format. In this example it is called requests.json
- Save requests.json in the same directory as your script

TODO:
====
- Create provider class
- Create Admin class
