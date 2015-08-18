#!/usr/bin/python
__author__ = 'https://github.com/chelnak'
import json

import requests

from helpers import authenticate, checkResponse
from prettytable import PrettyTable


class ConsumerClient(object):
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

    def getResource(self, id, show='json'):
        """
		Function that will get a vRA resource by id.
		Parameters:
            show = return data as a table or json object
			id = id of the vRA resource.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/resources/{id}'.format(host=host, id=id)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        resource = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Name', 'Status', 'Catalog Item'])
            table.add_row([
                resource['id'], resource['name'], resource['status'],
                resource['catalogItem']['label']
            ])

            print table

        elif show == 'json':
            return resource

    def getResourceByName(self, name, show='json'):
        """
        Function that will get a vRA resource by id.
        Parameters:
            show = return data as a table or json object
            name = name of the vRA resource.
        """

        host = self.host
        token = self.token

        url = "https://{host}/catalog-service/api/consumer/resources?$filter=name%20eq%20'{name}'".format(host=host, name=name)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        resource = r.json()

        if show == 'table':

            table = PrettyTable(['Id', 'Name', 'Status', 'Catalog Item'])
            table.add_row([
                resource['content'][0]['id'], resource['content'][0]['name'], resource['content'][0]['status'],
                        resource['content'][0]['catalogItem']['label']
                    ])

            print table

        elif show == 'json':
            return resource['content'][0]

    def getResourceIdByRequestId(self, id):
        """
		Function that will search for a resource with a matching requestId.
		Parameters:
			id = request id of the vRA resource.
		"""

        host = self.host
        token = self.token

        url = "https://{host}/catalog-service/api/consumer/resources?$filter=request%20eq%20'{id}'".format(host=host, id=id)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        resource = r.json()
        resourceId = resource['content'][0]['id']

        return resourceId

    def getAllResources(self, show='table', limit=20):
        """
		Function that will return all resources that are available to the current user.
        Parameters:
            show = return data as a table or json object
        	limit = The number of entries per page.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/resources?limit={limit}&$orderby=name%20asc'.format(
            host=host, limit=limit)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        resources = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Name'])

            for i in resources['content']:
                table.add_row([i['id'], i['name']])

            print table

        elif show == 'json':
            return resources['content']

    def getResourceNetworking(self, id, show='json'):
        """
		Function that will return networking information for a given resource.
		Parameters:
            show = return data as a table or json object
			id = id of the vRA resource.
		"""

        host = self.host
        token = self.token

        resource = self.getResource(id)
        resourceData = resource['resourceData']['entries']

        for i in resourceData:
            if i['key'] == 'NETWORK_LIST':
                networkList = i['value']['items']
                for j in networkList:
                    entries = j['values']['entries']

        if show == 'table':
            table = PrettyTable(['Component', 'Value'])

            for i in entries:
                table.add_row([i['key'], i['value']['value']])

            print table

        elif show == 'json':
            return entries

    def getEntitledCatalogItems(self, show='table', limit=20):
        """
		Function that will return all entitled catalog items for the current user.
        Parameters:
            show = return data as a table or json object
    		limit = The number of entries per page.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/entitledCatalogItems?limit={limit}&$orderby=name%20asc'.format(
            host=host, limit=limit)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        items = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Name'])

            for i in items['content']:
                table.add_row([i['catalogItem']['id'],
                               i['catalogItem']['name']])

            print table

        elif show == 'json':
            return items['content']

    def getRequest(self, id):
        """
		Function that will return request information for a given request.
		Parameters:
			id = the id of the vRA request.
            show = return data as a table or json object
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/requests/{id}'.format(host=host, id=id)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        request = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Request Number', 'Item', 'State'])
            table.add_row([request['id'], request['requestNumber'], request['requestedItemName'], request['state']])

            print table

        elif show == 'json':
            return request

    def getAllRequests(self, show='table', limit=20):
        """
		Function that will return the resource that were provisioned as a result of a given request.

		Parameters:
                show = return data as a table or json object
			    limit = The number of entries per page.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/requests?limit={limit}&$orderby=requestNumber%20desc'.format(host=host, limit=limit)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        items = r.json()

        if show == 'table':
            table = PrettyTable(['Id', 'Request Number', 'Item', 'State'])

            for i in items['content']:
                table.add_row([i['id'], i['requestNumber'], i['requestedItemName'], i['state']])

            print table

        elif show == 'json':
            return items['content']

    def getRequestResource(self, id):
        """
		Function that will return the resource that were provisioned as a result of a given request.
		Parameters:
			id = the id of the vRA request.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/requests/{id}/resources'.format(host=host, id=id)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        resource = r.json()

        return resource['content']

    def requestResource(self, payload):
        """
		Function that will submit a request based on payload.
		payload = json body (example in request.json)
		Parameters:
			payload = JSON request body.
		"""

        host = self.host
        token = self.token

        url = 'https://{host}/catalog-service/api/consumer/requests'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.post(url=url,
                          data=json.dumps(payload),
                          headers=headers,
                          verify=False)
        checkResponse(r)

        id = r.headers['location'].split('/')[7]

        return id
