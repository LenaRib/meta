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
    print(airtable_records)
    # for record in airtable_records:
    #     airtable_rows.append(record['id'])
    #     airtable_rows.append(record['fields'])
    # pd.DataFrame(airtable_rows)
    # for row in airtable_records:
    #     print(row['id'])
    return airtable_records
