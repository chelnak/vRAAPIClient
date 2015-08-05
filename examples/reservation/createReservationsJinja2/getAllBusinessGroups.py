#!/usr/bin/python

import json
import getpass
from vraapiclient import reservation
from globalconfig import url,usr,passwd

client = reservation.ReservationClient(url,usr,passwd)

client.getAllBusinessGroups()
