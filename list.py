# -*- coding: utf-8 -*-

isimler = ["alp","hasan","ali" ]

isimler.append("erkan")

print(isimler)

#isimler[0] = "efe"
print(isimler[2])
# list constructor
şehirler = list(("adana","mersin","erzincan"))

print(şehirler)

print(len(şehirler))

print(len(isimler))

#diğer fonksiyonlar

#print(şehirler.clear())
print("adana = " + str(şehirler.count("adana")))

print("adana indexi = " + str(şehirler.index("adana")))
şehirler.pop(0)
şehirler.reverse()
şehirler.insert(0,"izmir")

şehirler2 = şehirler
şehirler2[1] = "antalya"
şehirler3 = şehirler.copy()

şehirler.extend(şehirler2)
şehirler.sort()
şehirler.reverse()
print(şehirler)
