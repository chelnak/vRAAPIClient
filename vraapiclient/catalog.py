#!/usr/bin/python
__author__ = 'https://github.com/chelnak'

import json

import requests
from prettytable import PrettyTable

from helpers import authenticate, checkResponse


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

    def getResource(self, id):
        """
		Function that will get a vRA resource by id.
		Parameters:
			id = id of the vRA resource.
		"""

        host = self.host
        token = self.token

        url = 'https://' + host + '/catalog-service/api/consumer/resources/' + id
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)
        resource = r.json()

        return resource

    def getResourceId(self, id):
        """
		Function that will search for a resource with a matching requestId.
		Parameters:
			id = request id of the vRA resource.
		"""

        host = self.host
        token = self.token

        url = 'https://' + host + '/catalog-service/api/consumer/resources?$filter=request eq \'' + id + '\''
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

    def getAllResources(self, show='table'):
        """
		Function that will return all resources that are available to the current user.
		"""

        host = self.host
        token = self.token

        url = 'https://' + host + '/catalog-service/api/consumer/resources'
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

    def getResourceNetworking(self, id):
        """
		Function that will return networking information for a given resource.
		Parameters:
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
        return entries

    def getRequest(self, id):
        """
		Function that will return request information for a given request.
		Parameters:
			id = the id of the vRA request.
		"""

        host = self.host
        token = self.token

        url = 'https://' + host + '/catalog-service/api/consumer/requests/' + id
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': token
        }
        r = requests.get(url=url, headers=headers, verify=False)
        checkResponse(r)

        return r.json()

    def getEntitledCatalogItems(self, show='table'):
        """
		Function that will return all entitled catalog items for the current user.
		"""

        host = self.host
        token = self.token

        url = 'https://' + host + '/catalog-service/api/consumer/entitledCatalogItems'
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

    def requestResource(self, payload):
        """
		Function that will submit a request based on payload.
		payload = json body (example in request.json)
		Parameters:
			payload = JSON request body.
		"""

        host = self.host
        token = self.token

        url = 'https://' + host + '/catalog-service/api/consumer/requests'
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
