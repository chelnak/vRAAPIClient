#Welcome to vRAAPIClient

A python wrapper for the vRealize Automation REST API

Currently there is support for the following API endpoints:

* Catalog-Service Consumer API client: Request and view resources
* Reservation-Service API client: Create and view reservations

Responses will be in JSON or formatted in a table layout. This can be changed by
using the show="json" / show="table" parameter on some functions. This is not fully
implimented yet so make sure you read the classes to know which functions support
it.

Please see Basic Usage for some examples of this!

#vRA REST API Reference
This project has been built by following the vRA REST API Reference provided by
VMware.

Please take some time to familiarize yourself with it: [here](http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.restapi.doc/index.html)
