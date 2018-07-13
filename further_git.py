import requests
import json
import links_from_header
import csv
import os 


exampleFile = open('githubdata - Copy.csv' , encoding='utf-8')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
for i  in exampleData[1: ]:
    url= i[4]
    r = requests.get( url=url ,auth = ('user' , 'password' ))

    db = r.json()
    
    items = []
    for item in db:
        items.append('id')
    c = len(items)
    print(c)

