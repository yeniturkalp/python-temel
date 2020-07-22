# -*- coding: utf-8 -*-

#%%
x = int(input("kaç yıldız olsun ? = "))

yıldız = ""

for x in range(1, x + 1):
    yıldız = yıldız + "*"
    
    print(yıldız)
#%%    
# asal sayı

sayı = int(input("sayı giriniz"))
asalMı = True
for x in range(2,sayı):
   if (sayı % x ) == 0:
       asalMı = False
       break

if asalMı:
    print("ASAL")
else:
    print("ASAL DEĞİL")
    
    
    