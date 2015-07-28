#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import reservation

client = reservation.ReservationClient(url, usr, passwd)

with open('reservationTemplate.json') as json_data:
    payload = json.load(json_data)

reservation = client.createReservation(payload)

print "Reservation created: {id}".format(id=reservation)
