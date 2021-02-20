#!/usr/bin/env python

import requests

TABLE_NAME = 'Psychotherapists'
BASE_ID = 'apprk0Ir5niZ9pPNN'
API_KEY = 'keytSzf5K1JKexUfW'
URL = "https://api.airtable.com/v0/" + BASE_ID + "/" + TABLE_NAME
headers = {'Authorization': 'Bearer ' + API_KEY}
params = ()

response = requests.get(URL, params=params, headers=headers)
# get 100 records from Airtable
airtable_response = response.json()

airtable_rows = []
airtable_records = airtable_response['records']

# for record in airtable_records:
#     airtable_rows.append(record['id'])
#     airtable_rows.append(record['fields'])

# pd.DataFrame(airtable_rows)

for row in airtable_records:
    print(row['id'])
# insert ```airtable records into DB`
