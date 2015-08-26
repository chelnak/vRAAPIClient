#!/usr/bin/python
__author__ = 'https://github.com/chelnak'
import json

import requests

from helpers import authenticate, checkResponse
from prettytable import PrettyTable


class ReservationClient(object):
    #http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-7697320D-F3BD-4A42-8721-FBC971B47195.html
    def __init__(self, host, username, password, tenant=None):
        """
        Creates a connection to the vRA REST API using the provided
        username and password.
        Parameters:
            host = vRA Appliance fqdn
            user = user account with access to the vRA portal
            passowrd = valid password for above user
            tenant = tenant for user. if this is NONE it will default to "vsphere.local"
        """

        if tenant is None:
            tenant = "vsphere.local"

        self.host = host
        self.username = username
        self.password = password
        self.tenant = tenant
        self.token = authenticate(host, username, password, tenant)

    def getToken(self):
        """
		Function that prints the bearer token for the session.
		This is only for troubleshooting.
		"""

        print self.token

    def getAllBusinessGroups(self, tenant=None, show='table', limit=20):
        """
        Get All business groups
		List ID and name for each business group
        Parameters:
            tenant = vRA tenant. if null then it will default to vsphere.local
            show = return data as a table or json object
            limit = The number of entries per page.
        """

        host = self.host
        token = self.token

        if tenant is None:
            tenant = "vsphere.local"

        url = 'https://{host}/identity/api/tenants/{tenant}/subtenants?limit={limit}&$orderby=name'.format(
            host=host, tenant=tenant, limit=limit)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        businessGroups = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Name'])

            for i in businessGroups['content']:
                table.add_row([i['id'], i['name']])

            print table
        elif show == 'json':
            return businessGroups['content']

    def getReservation(self, reservationid, show='table'):
        """
		Verify a reservation and get reservation details
		http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-2A2D96DE-9BBE-414B-82AB-DD70B82D3E0C.html
		Parameters:
			reservationid = Id of a new or existing reservation
            show = return data as a table or json object
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/reservations/{reservationid}'.format(host=host, reservationid=reservationid)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        reservation = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Name'])
            table.add_row([
            reservation['id'], reservation['name']])

            print table

        elif show == 'json':
            return reservation

    def getReservationByName(self, name, show='table'):
        """
        Get a reservation by name
        Parameters:
            name = name of a new or existing reservation
            show = return data as a table or json object
        """

        host = self.host
        token = self.token

        url = "https://{host}/reservation-service/api/reservations?$filter=name%20eq%20'{name}'".format(host=host, name=name)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        reservation = r.json()

        if show == 'table':
                    table = PrettyTable(['Id', 'Name'])
                    table.add_row([
                        reservation['content'][0]['id'], reservation['content'][0]['name']])

                    print table

        elif show == 'json':
                return reservation['content'][0]

    def getAllReservations(self, show='table', limit=20):
        """
		Get all reservations
		Parameters:
			show = Output either table format or raw json
            limit = The number of entries per page.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/reservations?limit={limit}'.format(
            host=host, limit=limit)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        reservations = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Name'])

            for i in reservations['content']:
                table.add_row([i['id'], i['name']])

            print table
        elif show == 'json':
            return reservations['content']

    def createReservation(self, payload):
        """
		Creating a reservation by type
		http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-11510887-0F55-4EA4-858C-9881F94C718B.html
		Parameters:
			payload = JSON payload containing the reservation information
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/reservations'.format(host=host)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.post(url=url,
                          headers=headers,
                          data=json.dumps(payload),
                          verify=False)
        checkResponse(r)

        reservationId = r.headers['location'].split('/')[6]

        return reservationId

    def getReservationTypes(self):
        """
		Display a list of supported reservation types:
		http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-57F7623F-6740-49EC-A572-0525D56862F1.html
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/reservations/types'.format(host=host)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        reservationTypes = r.json()

        return reservationTypes[u'content']

    def getReservationSchema(self, schemaclassid):
        """
		Displaying a schema definition for a reservation
		http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-E957942A-1CCC-4C16-8147-0F5D382CDCB5.html
		Parameters:
			schemaclassid = schemaClassId of supported reservation Type. E.g Infrastructure.Reservation.Virtual.vSphere
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/data-service/schema/{schemaclassid}/default'.format(host=host, schemaclassid=schemaclassid)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        reservationSchema = r.json()

        return reservationSchema[u'fields']

    def getBusinessGroupId(self, tenant=None, buisenessGroupName=None):
        """
		Get the business group ID for a reservation
		http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-588865AE-0134-4087-B090-C725790C052C.html
		Parameters:
			tenant = vRA tenant. if null then it will default to vsphere.local
			businessGroupName = For future use. Need to be able to fetch ID from business group name
		"""

        host = self.host
        token = self.token

        if tenant is None:
            tenant = "vsphere.local"

        url = 'https://{host}/identity/api/tenants/{tenant}/subtenants'.format(host=host, tenant=tenant)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        businessGroupId = r.json()

        return businessGroupId

    def getComputeResourceForReservation(self, schemaclassid):
        """
		Get a compute resource for the reservation
		http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-AF6F177D-13C2-47AD-842D-1D341591D5F4.html
		Parameters:
			schemaclassid = schemaClassId of supported reservation Type. E.g Infrastructure.Reservation.Virtual.vSphere
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/data-service/schema/{schemaclassid}/default/computeResource/values'.format(host=host, schemaclassid=schemaclassid)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        payload = {}
        r = requests.post(url=url,
                          headers=headers,
                          data=json.dumps(payload),
                          verify=False)
        checkResponse(r)

        computeResource = r.json()

        return computeResource

    def getResourceSchemaForReservation(self, schemaclassid, fieldid,
                                        computeresourceid):
        """
		Getting a resource schema by reservation type
		#http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-C19E4316-603F-4497-86DB-C241ECE4EEB4.html
		vSphere reservation syntax: http://pubs.vmware.com/vra-62/index.jsp#com.vmware.vra.programming.doc/GUID-CAB141B4-E25F-42EC-B2C4-8516366CB43F.html
		Parameters:
			schemaclassid = schemaClassId of supported reservation Type. E.g Infrastructure.Reservation.Virtual.vSphere
			fieldid = Extension field supported in the reservation... E.g resourcePool
			computeresourceId = Id of the compute resource to query
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/reservation-service/api/data-service/schema/{schemaclassid}/default/{fieldid}/values'.format(host=host, schemaclassid=schemaclassid, fieldid=fieldid)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        payload = {
            "text": "",
            "dependencyValues": {
                "entries": [{
                    "key": "computeResource", "value": {
                        "type": "entityRef", "componentId": 'null', "classId":
                        "ComputeResource", "id": "{computeResourceId}".format(
                            computeResourceId = computeresourceid)
                    }
                }]
            }
        }

        r = requests.post(url=url,
                          headers=headers,
                          data=json.dumps(payload),
                          verify=False)
        checkResponse(r)
        resourceSchema = r.json()

        return resourceSchema
