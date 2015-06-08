import getpass
import json

from jinja2 import Environment, FileSystemLoader

from vraapiclient import vRAAPIReservationClient

url = ''
usr = ''
passwd = getpass.getpass()

#Create a new Reservation-Service API client
client = vRAAPIReservationClient(url, usr, passwd)

#Set up jinja2 environment
#jinja2 will look inside the templates folder for the json file
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('vsphere_reservation.json')

#Set all configurable parameters here
params = {
    'ReservationName': 'JINJA2-API-Reservation',
    'ReservationEnabled': 'true',
    #Booleans - couldn't get it to work with jinja2
    'TenantId': 'vsphere.local',
    'BusinessGroupId': '',
    'ResourcePoolLabel': '',
    'ResourcePoolId': '',
    'ComputeResourceLabel': '',
    'ComputeResourceId': '',
    'ComputeResourceReservedMemMb': '',
    'MachineQuota': '',
    'NetworkLabel': '',
    'NetworkId': '',
    'VCNSSecurityGroupLabel': '',
    'VCNSSecurityGroupId': '',
    'AlertEnabled': 'true',  #Booleans - couldn't get it to work with jinja2
    'AlertFrequency': '1',
    'AlertStoragePercent': '80',
    'AlertMemoryPercent': '80',
    'AlertCPUPercent': '80',
    'AlertMachinePercent': '80',
    'AlertRecepients': 'test@company.com',
    'AlertEmailMgr': 'true',  #Booleans - couldn't get it to work with jinja2
    'StorageLabel0': '',
    'StorageId0': '',
    'StorageSizeGB0': '250',
    'StorageReservationPriority0': '0',
    'StorageEnabled0': 'true'  #Booleans - couldn't get it to work with jinja2
}

#Create the JSON payload for the POST
payload = json.loads(template.render(params=params))

#Create a new reservation
reservation = client.createReservation(payload)
print "Reservation id: " + reservation

#Get all Reservations
#client.getAllReservations()

#Get all Business Groups
#client.getAllBusinessGroups()

#Get a Reservation
reservation = client.getReservation(reservation)
print reservation
