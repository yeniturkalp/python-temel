# -*- coding: utf-8 -*-

def selamver (isim = " ziyaretçi "):
    print(isim + "merhaba")
    
selamver()    


def selamver2 (isim = " ziyaretçi " , soyisim = "  yenitürk "):
    print(isim +  soyisim   + " " + " merhaba " )

selamver2("alpaslan")        
selamver(" alpaslan "  " yenitürk " )

#%%

def üçgenalanıhesapla(a,b):
    return a*b/2

alan = üçgenalanıhesapla(3,6)
print(alan)

#%%

üçgenalanhesapla2 = lambda a,b : a*b/2
print(üçgenalanhesapla2(3,6))

x = üçgenalanhesapla2

print(x(5,7))