# -*- coding: utf-8 -*-




try:
    sayı = int(input("Sayı giriniz = "))
except ValueError:
    print("Tip uyuşmazlığı : Lütfen sayı giriniz")
except ZeroDivisionError:
    print("Payda sıfır olamaz")
except:
    print("Hata Oluştu")
    
    
    