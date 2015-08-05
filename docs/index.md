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

Please take some time to familiarize yourself with it: [here](http://pubs.vmware.com/vra-62/index.jsp?topic=%2Fcom.vmware.vra.restapi.doc%2Findex.html&__utma=207178772.178252748.1437379173.1438264451.1438768134.5&__utmb=207178772.1.10.1438768134&__utmc=207178772&__utmx=-&__utmz=207178772.1438264451.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)&__utmv=-&__utmk=137532467)
