#!/usr/bin/python
import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import reservation

client = reservation.ReservationClient(url, usr, passwd)

reservationName = 'vracl-res-01'

#Print table
client.getReservationByName(name=reservationName)

#Get JSON Object
reservation = client.getReservationByName(name=reservationName, show='json')

#Print id and name
print reservation['id']
print reservation['name']

#Use json.dumps() to get json string
reservationJSONString = json.dumps(reservation)
print reservationRaw

#Use json.dumps() to get json string
entitledCatalogItemsJSONString = json.dumps(entitledCatalogItems)
print entitledCatalogItemsJSONString
