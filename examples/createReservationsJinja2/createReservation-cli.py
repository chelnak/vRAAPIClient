#!/usr/bin/python

import getpass
import json
import os

from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader
from vraapiclient import reservation


def getArgs():

    parser = ArgumentParser(
        description='Create a vRA Reservation with vRAAPIClient')
    parser.add_argument('-n', '--reservationName',
                        help='Name for the reservation',
                        required=True)
    parser.add_argument('-s', '--subTenantId',
                        help='Subtenant Id',
                        required=True)
    parser.add_argument('-u', '--user', help='Subtenant Id', required=True)
    parser.add_argument('-p', '--password',
                        help='Subtenant Id',
                        required=False)
    parser.add_argument('--url', help='Subtenant Id', required=True)
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = getArgs()
    reservationName = args.reservationName
    subtenantId = args.subTenantId
    usr = args.user
    passwd = args.password
    url = args.url

    if not passwd:
        passwd = getpass.getpass()

    #Get the current directory
    currentDirectory = os.path.dirname(os.path.abspath(__file__))

    client = reservation.ReservationClient(url, usr, passwd)

    #Set up jinja2 environment
    env = Environment(loader=FileSystemLoader(currentDirectory))
    template = env.get_template('reservationTemplate.json')

    #Set all configurable parameters here
    params = {'ReservationName': reservationName, 'SubTenantId': subtenantId, }

    #Create the JSON payload for the POS
    #This is where params are added to the json payload

    payload = json.loads(template.render(params=params))

    reservation = client.createReservation(payload)

    print "Reservation created: {id}".format(id=reservation)
