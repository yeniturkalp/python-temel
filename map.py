# -*- coding: utf-8 -*-

sayılar = [1,2,3,4,5]

sayılarkareli = list(map(lambda x: x**2,sayılar ))

#sayılarkareli = []
#
#for sayı in sayılar:
#    sayılarkareli.append(sayı*sayı)
    


sayılarfiltreli = list(filter(lambda x: x>2,sayılar))


print(sayılarkareli)
print(sayılarfiltreli)


from functools import reduce

sayılarFaktoriyel = reduce(lambda x,y:x*y,sayılar)

print(sayılarFaktoriyel)