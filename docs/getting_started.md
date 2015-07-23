#Dependencies
The following dependencies are required for vRAAPIClient to work and will be installed
automatically when you run setup.py

* requests http://docs.python-requests.org/en/latest/
* prettytable https://code.google.com/p/prettytable/

#Basic Installation
Installation is fairly simple. Start by cloning the github repo then install using
the setup.py file provided

```
git clone https://github.com/chelnak/vRAAPIClient.git
cd vRAAPIClient
python setup.py install
```

#Installation with virtualenv
Sometimes its nice to know that your python projects are isolated. This is why I like to
use virtualenv.

See [here](https://virtualenv.pypa.io/en/latest/) for the latest virtualenv docs

```
pip install virtualenv
mkdir vRAAPIClient-Scripts
cd vRAAPIClient-Scripts
virtualenv venv
source venv/bin/activate
git clone https://github.com/chelnak/vRAAPIClient.git
cd vRAAPIClient
python setup.py install
```

You can then run pip freeze to see what has been installed

#Basic Usage

##Consumer API

```
#!/usr/bin/python
import getpass
import json

from vraapiclient import catalog

url = ''
usr = ''
passwd = getpass.getpass()

#Create a new consumer API client
client = catalog.ConsumerClient(url, usr, passwd)

#Print out a table of all entitled catalog items for the current user
client.getEntitledCatalogItems()

#Or get the response in JSON so you can decided how to parse the data
r = client.getEntitledCatalogItems(show="json")
print r

```

##Reservation Service API

```
#!/usr/bin/python
import getpass
import json

from vraapiclient import reservation

url = ''
usr = ''
passwd = getpass.getpass()

client = client.ReservationClient(url, usr, passwd)

#Print out a table of all reservations
client.getAllReservations()

#Or get the response in JSON so you can decided how to parse the data
r = client.getAllReservations(show="json")
print r



```
