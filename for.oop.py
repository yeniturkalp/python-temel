# -*- coding: utf-8 -*-

sehirler = ["izmir","adana","bayburt","bursa"]
#
#print(sehirler[0])
#print(sehirler[1])
#print(sehirler[2])
#print(sehirler[3])

#%% for intro

for sehir in sehirler:
    if sehir == "bayburt":
#       break
#        continue
    print(sehir + " için kod = " + sehir[0:3] )
    print("**********")    
 
    
#%% for range
for x in range(1,100,2):
    print(x + 1)