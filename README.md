vRAAPIClient
============

A python wrapper for the vRealize Automation REST API

- ConsumerAPI client: Request and view resources
- ReservationServiceAPI client: Create and view reservations

Returns API responses in JSON format

Dependencies:
===========
- requests: http://docs.python-requests.org/en/latest/
- prettytable https://code.google.com/p/prettytable/

Basic usage:
============
Consumer API:
-------------
```
#!/usr/bin/python
import getpass
import json

from vraapiclient import catalog

url = ''
usr = ''
passwd = getpass.getpass()

#Create a new consumer API client
client = catalog.ConsumerClient(url, usr, passwd)

#print out a table of all entitled catalog items for the current user
client.getEntitledCatalogItems()
```

Reservation Service API:
------------------------
```
#!/usr/bin/python
import getpass
import json

from vraapiclient import catalog

url = ''
usr = ''
passwd = getpass.getpass()

client = client.ReservationClient(url, usr, passwd)

client.getAllReservations()
```

TODO:
====
- Create provider class
- Create admin class
- Better error handling
- Boolean support with jinja?
- Better docs

Change log:
===========
01/06/2015
- Added setup.py to make installation easier
- Moved to a module based structure
- More code cleanups

06/05/2015:
- Added: Reservation service API client based on the steps here -> http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-11510887-0F55-4EA4-858C-9881F94C718B.html
- Reservation_example.py and templates/vsphere_reservation.json. Contains examples of how to use the vRAAPIAPIReservationClient with jinja2 templates
- Implemented PrettyTables for formatting outputs of some functions.. The plan is to back port these in to the vRAAPIConsumerClient
