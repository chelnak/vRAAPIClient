#18/08/2015
* Version 1.0.2.4
* Fixed issue with getResourceIdByRequestId and a missing double quote
* Fixed issue with getAllRequests.py example
* Added acceptedResponses = [200, 201, 203, 204] to helpers.py

#17/08/2015
* Version 1.0.2.3
* Added catalog.getResourceByName() with examples and docs
* Added catalog.getRequestResouce added docs and updated requestResourceAndWait examples
* Added catalog.getAllRequests with examples and docs
* Added reservation.getReservationByName with examples and docs

##16/08/2015
* Version 1.0.2.2
* Merged pull request from
* Moved to str.format
* Added $&orderby=name to reservation.getAllBusinessGroups & reservation.getAllReservations
* Noticed that orderby does not work for getAllReservations <- turns out this is not supported by the vRA API

##06/08/2015
* Version 1.0.1
* Added show option to catalot.getResource and catalog.getResourceNetworking()
* Updated docs

##05/08/2015
* Added documentation for the catalog ConsumerClient
* Changed getResourceId to getResourceIdByRequestId in catalog.py
* Fixed table print issue for getAllResources in catalog.py

##22/07/2015
* Making a start on some documentation

##01/06/2015
* Added setup.py to make installation easier
* Moved to a module based structure
* More code cleanups

##06/05/2015
* Added: Reservation service API client based on the steps here http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-11510887-0F55-4EA4-858C-9881F94C718B.html
* Reservation_example.py and templates/vsphere_reservation.json. Contains examples of how to use the vRAAPIAPIReservationClient with jinja2 templates
* Implemented PrettyTables for formatting outputs of some functions.. The plan is to back port these in to the vRAAPIConsumerClient
