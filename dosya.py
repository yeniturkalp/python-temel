# -*- coding: utf-8 -*-

#f = open("costumer2.txt")
#print(f.read())
#
#
#for l in f:
#    print(l)
#    
#f.close()    


fileToAppend = open("öğrenciler.txt","a")
fileToAppend.write("\n")
fileToAppend.write("hasan")
fileToAppend.close()

#%%

import os 

if os.path.exists("öğrenciler.txt"):
    os.remove("öğrenciler.txt")
    
else:
    print("dosya mevcut değil")



os.rmdir("klasör")