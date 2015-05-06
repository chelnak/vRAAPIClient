vRAAPIClient
============

A python wrapper for the vRealize Automation REST API

Created for two reasons:
- because
- Cloudclient is great, but I like APIs and needed information that it did not provide at the time of writing

Returns API responses in JSON format

Dependencies:
===========
- requests: http://docs.python-requests.org/en/latest/

Basic usage:
============

from vraapiclient import vRAAPIConsumerClient

url = "vra host"
usr = "user"
pass = "pass"

client = vRAAPIConsumerClient(url, usr, passwd)

resources = client.getAllResources()

print resources

example.py:
==========
- chmod +x example.py
- ./example.py
- You must create a file containing the request data in JSON format. In this example it is called requests.json
- Read the following blog to learn how to caputre postData for the request: http://grantorchard.com/vcac/concepts/exploring-vcac-api-part-1/
- Save requests.json in the same directory as your script

TODO:
====
- Create provider class
- Create admin class
