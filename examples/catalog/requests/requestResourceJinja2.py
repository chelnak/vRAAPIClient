#!/usr/bin/python
import getpass
import json
import os

from jinja2 import Environment, FileSystemLoader
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

request = client.requestResource(payload)

print "Request submitted: {id}".format(id=request)
