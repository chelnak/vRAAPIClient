#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import reservation

client = reservation.ReservationClient(url, usr, passwd)

#You will first need to get the id of your template reservation
#The best way to do this is by listing all of the reservations you have
#Run getAllReservations.py

reservationId = 'your-reservation-id-here'

#Get the reservation
reservation = client.getReservation(reservationId)

#Parse the response with json.loads so it looks right when we write out to a file
reservationTemplate = json.loads(reservation)

#Write out the parsed json to reservationTemplate.json
with open('reservationTemplate.json', 'w') as t:
    json.dump(reservationTemplate, t, indent=4)

#IMPORTANT:
#Before you use the template to create a reservation, remove the ID from the bottom of the file
