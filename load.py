#!/usr/bin/env python

import requests
import pandas as pd

TABLE_NAME = 'Psychotherapists'
BASE_ID = 'apprk0Ir5niZ9pPNN'
API_KEY = 'keytSzf5K1JKexUfW'
URL = "https://api.airtable.com/v0/" + BASE_ID + "/" + TABLE_NAME
headers = {'Authorization': 'Bearer ' + API_KEY}
params = ()

response = requests.get(URL, params=params, headers=headers)
airtable_response = response.json()
# first 100 recored only

airtable_rows = []
airtable_records = airtable_response['records']
for record in airtable_records:
    airtable_rows.append(record['fields'])
pd.DataFrame(airtable_rows)

print(airtable_rows)


def setUp(self):
    self.base_id = BASE_ID
    self.api_key = API_KEY
    self.airtable = airtable.Airtable(self.base_id, self.api_key)


def get(self, *args, **kwargs):
    return self.airtable.get(TABLE_NAME, *args, **kwargs)
