#!/usr/bin/env python

import requests
from baseproject.settings import API_KEY, URL

headers = {'Authorization': 'Bearer ' + API_KEY}
params = ()


def getAirtableRec():
    response = requests.get(URL, params=params, headers=headers)
    # get 100 records from Airtable
    airtable_response = response.json()
    airtable_records = airtable_response['records']
    # todo add data preparation (id: {name: , photo: full url, metods: [] }) - id is unique and should be a key
    return airtable_records
