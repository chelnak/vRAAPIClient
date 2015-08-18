#!/usr/bin/python
__author__ = 'https://github.com/chelnak'
import json
import sys

import requests


def checkResponse(r):
    """
	Quick logic to check the http response code.

	Parameters:
		r = http response object.
	"""

    acceptedResponses = [200, 201, 203, 204]
    if not r.status_code in acceptedResponses:
        print "STATUS: {status} ".format(status=r.status_code)
        print "ERROR: " + r.text
        sys.exit(r.status_code)


def authenticate(host, user, password, tenant):
    """
	Function that will authenticate a user and build.

	Parameters:
		host = vRA Appliance fqdn.
		user = user account with access to the vRA portal.
		passowrd = valid password for above user.
		tenant = tenant for the user.
	"""

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    payload = {"username": user, "password": password, "tenant": tenant}
    url = 'https://' + host + '/identity/api/tokens'
    r = requests.post(url=url,
                      data=json.dumps(payload),
                      headers=headers,
                      verify=False)
    checkResponse(r)
    response = r.json()

    usr_token = 'Bearer ' + response['id']

    return usr_token
