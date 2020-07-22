# -*- coding: utf-8 -*-

import json

with open("users.json") as users:
    data = json.load(users)
    
    
for x in range(9):
    print(data[x]["address"]["geo"]["lat"])








#print(data[0]["address"]["geo"]["lat"]) 

   