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

from vraapiclient import vRAAPIConsumerClient

url = "vra host"
usr = "user"
pass = "pass"

client = vRAAPIConsumerClient(url, usr, passwd)
resources = client.getAllResources()
print resources

Reservation Service API:

from vraapiclient import vRAAPIReservationClient

url = "vra host"
usr = "user"
pass = "pass"

client = vRAAPIReservationClient(url, usr, passwd)
client.getAllReservations()

Example Scripts:
==========
- chmod +x example.py
- ./example.py

- Resource example:
- You must create a file containing the request data in JSON format. In this example it is called requests.json
- Read the following blog to learn how to caputre postData for the request: http://grantorchard.com/vcac/concepts/exploring-vcac-api-part-1/
- Save requests.json in the same directory as your script

- Reservation example:
- Uses jinja2 to render variables from a dict to the json file in templates/vsphere_reservation.json
- The best way to create a reservation is to use an existing one as a template:
	- Get a list of all reservations -> client.getAllReservations
	- Take the Id of the reservation you want to copy, get your JSON response and save it to a file -> reservation = client.getReservation(reservationId)
	- Be sure to validate your JSON :-)
	- Remove the id field from the bottom of the file which refers to the reservation you are copying
	- Replace all values with jinja references you wish to dynamically change, e.g. {{ params.BusinessGroupId }}, based on the example in templates/vsphere_reservation.json
	- Use reservations_example.py as a reference

TODO:
====
- Create provider class
- Create admin class
- Better error handling
- Boolean support with jinja?
- Better docs

Change log:
===========
06/05/2015:
	- Added: Reservation service API client based on the steps here -> http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-11510887-0F55-4EA4-858C-9881F94C718B.html
	- Reservation_example.py and templates/vsphere_reservation.json. Contains examples of how to use the vRAAPIAPIReservationClient with jinja2 templates
	- Implemented PrettyTables for formatting outputs of some functions.. The plan is to back port these in to the vRAAPIConsumerClient
