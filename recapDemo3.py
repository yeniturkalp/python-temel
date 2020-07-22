# -*- coding: utf-8 -*-

import sys

liste = [8, " alp ", 9 ," ali ",0 , "6"]

for x in liste:
    try:
        print("Sonuç = "+ str(x))
        sonuç = 1/int(x)    
        print("Sonuç = "+ str(x))
    
    except ValueError :
        print(str(x) + "bir sayı değil")
    except ZeroDivisionError :
        print(str(x) + " için sıfıra bölme hatası ")
    except:
        print(str(x)+ "hesaplanamadı")
        print("Sistem diyor ki :" + str(sys.exc_info()[0] ))
    finally:
        print("işlemler bitti ")