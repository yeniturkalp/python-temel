# -*- coding: utf-8 -*-
# Substring

message = "Gelecek yüzyıl"

print(message[2:5])

newmessage = message[:5]
print(newmessage[:1]) 
print(type(message))

# Len
print(len(message))
newmessage2 = message[len(message)-1 : len(message)]

print(newmessage2)

# Lower/upper
print(message.upper())
print(message.lower())

#Replace
print(message)
print(message.replace("G","i"))

#strip/split

bilgi = "  alpaslan,yenitürk,19,bursa   "

print(bilgi.upper())
print(bilgi.split(",")) 

print(" AD = " + bilgi.split(",")[0])

#input

ad = input("adınız?")

sayı1= input("sayı1 =?")
sayı2= input("sayı2=?")

print(int(sayı1)+int(sayı2))














