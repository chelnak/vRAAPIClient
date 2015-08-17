#ConsumerClient

##getAllBusinessGroups

Return all Business Groups.

###Parameters
* [string]show = This determines what is returned. Use json to return a json object or
                    table to return a table. This parameter is not mandatory.
* [int]limit = This determines how many entries are returned. If not specified,
                    it will default to 20.

By default this function will return a table containing the id and name of the
resource.

```
client.AllBusinessGroups()
```

This can be changed by adding the show parameter as follows:

```
businessGroups = client.getAllBusinessGroups(show='json')
```

show='json' will return an object. You can interact with this object in the same way
that you would with any object.

```
businessGroups = client.getAllBusinessGroups(show='json')

for businessGroup in businessGroups:

  print businessGroup['id']
  print businessGroup['name']
```

If you want to return a json string, you will need to use json.dumps().

```
businessGroups = client.getAllBusinessGroups(show='json')
businessGroupJSONString = json.dumps(businessGroups)
print businessGroupJSONString
```

##getAllReservations  

Get all reservations

###Note from the API Doc:
* Filtering is only supported on 'name,'reservationTypeId', 'subTenantId', 'enabled', 'tenantId' and 'reservationPolicyId'
* sorting is not supported

###Parameters
* [string]show = This determines what is returned. Use json to return a json object or
                    table to return a table. This parameter is not mandatory.
* [int]limit = This determines how many entries are returned. If not specified,
                    it will default to 20.

By default this function will return a table containing the id and name of the
resource.

```
client.getAllReservations()
```

This can be changed by adding the show parameter as follows:

```
reservations = client.getAllReservations(show='json')
```

show='json' will return an object. You can interact with this object in the same way
that you would with any object.

```
reservations = client.getAllReservations(show='json')

for reservation in reservations:

  print reservation['id']
  print reservation['name']
```

If you want to return a json string, you will need to use json.dumps().

```
reservations = client.getAllReservations(show='json')
reservationsJSONString = json.dumps(reservations)
print reservationsJSONString
```

##getReservation

Retrieve a reservation

###Parameters
* [string]id = the id of the vRA reservation
* [string]show = This determines what is returned. Use json to return a json object or
                    table to return a table. This parameter is not mandatory.

By default this function will return a table containing the id and name of the resource.

```
reservationId = '171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
client.getAllReservations(reservationid = reservationId)
```

This can be changed by adding the show parameter as follows:

```
reservationId = '171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
reservation = client.getAllReservations(id=reservationId, show='json')
```

show='json' will return an object. You can interact with this object in the same way
that you would with any object.

```
print reservation['id']
print reservation['name']
```

If you want to return a json string, you will need to use json.dumps().

```
reservationId = '171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
reservation = client.getAllReservations(id=reservationId, show='json')
reservationJSONString = json.dumps(reservation)
print reservationJSONString
```

##getReservationByName

Get a vRA reservation by name

###Parameters
* [string]name = name of the vRA reservation
* [string]show = This determines what is returned. Use json to return a json object or
                    table to return a table. This parameter is not mandatory.

You can display data from this function in a table as follows:

```
reservationeName='vra-cl-res-01'
client.getReservationByName(name=reservationeName, show='table')
```

By default this function will return a json object. You can interact with this object in the same way
that you would with any object.

```
reservationeName='vra-cl-res-01'
reservation = client.getReservationByName(name=reservationeName, show='json')
print reservation['id']
print reservation['name']
```

If you want to return a json string, you will need to use json.dumps().

```
reservationeName='vra-cl-res-01'
reservation = client.getReservationByName(name=reservationeName, show='json')
reservationJSONString = json.dumps(reservation)
print reservationJSONString
```

##createReservation

Create a new reservation

###Parameters
* [json]payload = json request (example: reservationTemplate.json).

Before using this template, you will need to create a reservatin template.

To do this, follow the steps in Creating a Reservation Template below.

###Basic example
```
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
```

For more detailed examples please see the examples/reservation directory of this project

##Creating a Reservation Template

From experience, I have found that that the best thing to do when programatically creating
reservations is to use an existing one as a template.

For steps on how to create your own template, please follow the steps in [this blog post](http://www.craiggumbley.co.uk/2015/07/creating-vrealize-automation.html).
