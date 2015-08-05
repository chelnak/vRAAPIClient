#!/usr/bin/python
import getpass
import json
import os

from globalconfig import passwd, url, usr
from jinja2 import Environment, FileSystemLoader
from vraapiclient import reservation

#Get the current directory
currentDirectory = os.path.dirname(os.path.abspath(__file__))

client = reservation.ReservationClient(url, usr, passwd)

#Set up jinja2 environment
env = Environment(loader=FileSystemLoader(currentDirectory))
template = env.get_template('reservationTemplate.json')

#Get all business groups
businessGroups = client.getAllBusinessGroups(show="json")

#Loop through each group in the businessGroups object and pull out
#id and name, format the reservation name and inject both values
#in to the params dict.
for group in businessGroups:

        #This is where we format the reservation name.
        #[ComputeResource]-Res-BusinessGroupName(nospaces)
        name = 'CLTEST01-Res-{groupname}'.format(groupname = group['name'].replace(" ",""))

        #Set all configurable parameters here
        params = {
                'ReservationName': name,
                'SubTenantId': group['id'],
        }

        #Create the JSON payload for the POST
        #This is where params are added to the json payload
        payload = json.loads(template.render(params=params))

        #Attempt to create each reservation. Catch any errors and continue
        try:
                reservation = client.createReservation(payload)
                print "Reservation created: {id}".format(id=reservation)

        except Exception, e:

            pass
