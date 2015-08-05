#!/usr/bin/python

import getpass
import json
import os

from jinja2 import Environment, FileSystemLoader
from globalconfig import url, usr, passwd
from vraapiclient import reservation

#Get the current directory
currentDirectory = os.path.dirname(os.path.abspath(__file__))

client = reservation.ReservationClient(url, usr, passwd)

#Set up jinja2 environment
env = Environment(loader=FileSystemLoader(currentDirectory))
template = env.get_template('reservationTemplate.json')

#Set all configurable parameters here
params = {
    'ReservationName': 'CL-Res-TEST-JINJA2-01',
    'SubTenantId': 'ad0073e7-401f-4a39-ac84-519a891a13ff',
}

#Create the JSON payload for the POST
#This is where params are added to the json payload

payload = json.loads(template.render(params=params))

reservation = client.createReservation(payload)

print "Reservation created: {id}".format(id=reservation)
