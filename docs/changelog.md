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
