# -*- coding: utf-8 -*-

setA = {1,2,5,4,7}
setB = {11,7,5,9,8,4}

print(setA | setB)
print(setA.union(setB))



print(setA & setB)
print(setA.intersection(setB))

print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference_update(setA))