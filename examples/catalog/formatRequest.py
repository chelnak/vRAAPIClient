#!/usr/bin/python

#Quick script to format request from vRA

import json

with open('request.json','r') as f:

	f = json.load(f)

	with open ('requestFormatted.json', 'w') as g:
		json.dump(f,g, indent=4)
