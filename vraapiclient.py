#!/usr/bin/python

from __future__ import unicode_literals
import requests, json
import sys

#TODO - add external config file
vcac_hostname = ""
usr = ""
usr_pass = ""
default_tenant = ""

def checkResponse(r):
	#Quick logic to check the http response code
	if r.status_code != 200:
		print "STATUS: {status} ".format(status=r.status_code)
		print "ERROR: " + r.text
		sys.exit(r.status_code)

def authenticate(host, user, password, tenant):
	#Build POST for authentication
	headers = { 'Content-Type' : 'application/json', 'Accept' : 'application/json'}

	payload = {"username": user, "password": password, "tenant": tenant}

	url = 'https://'+ host + '/identity/api/tokens'

	#Send Request
	req = requests.post(url = url, data = json.dumps(payload), headers = headers, verify = False)

	#Check request response is 200
	checkResponse(req)

	#Get JSON response
	response =  req.json() 

	#Build bearer token
	usr_token = 'Bearer ' + response[u'id']

	return usr_token


class vRAAPIClient(object):
	def __init__(self, host, username, password, tenant=None):
		if tenant is None:
			tenant = "vsphere.local"

		self.host = host
		self.username = username
		self.password = password
		self.tenant = tenant
		self.token = authenticate(host, username, password, tenant)

	def getResource(self, id):
		host = self.host
		token = self.token
		
		url = 'https://' + host + '/catalog-service/api/consumer/resources/' + id
		headers = { 'Content-Type' : 'application/json', 'Accept' : 'application/json', 'Authorization' : token}
		req = requests.get(url = url, headers = headers, verify = False)
		checkResponse(req)
		resource = req.json()
	
		return resource

	def getAllResources(self):
		host = self.host
		token = self.token

		url = 'https://' + host + '/catalog-service/api/consumer/resources'
		headers = { 'Content-Type' : 'application/json', 'Accept' : 'application/json', 'Authorization' : token}
		req = requests.get(url = url, headers = headers, verify = False)
		checkResponse(req)
		resources = req.json()

		return resources[u'content']
	
	def getToken(self):
		print self.token
	
	def getResourceNetworking(self, id):
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
