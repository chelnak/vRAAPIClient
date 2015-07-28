#!/usr/bin/python

import getpass
import json

from globalconfig import passwd, url, usr
from vraapiclient import reservation

client = reservation.ReservationClient(url, usr, passwd)

client.getAllReservations()
