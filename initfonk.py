# -*- coding: utf-8 -*-
#%% 
class MATEMATİK:
    def __init__(self,sayı1,sayı2):
        self.sayı1 = sayı1
        self.sayı2 = sayı2
    def topla(self):
        return self.sayı1 + self.sayı2
    
    def çıkarma(self):
        return self.sayı1 - self.sayı2
    
    def çarp(self):
        return self.sayı1 * self.sayı2
    
    def bölme(self):
        return self.sayı1 / self.sayı2
    
matematik = MATEMATİK(18,2)
matematik2 = MATEMATİK(20,5)

print(" SONUÇ = " + str(matematik2.bölme()))    

#%% PROPERTY

class Person:
    def __init__(self,firstName,lastName,Age):
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age 
        
person = Person("alpaslan","yenitürk",19)
print(person.firstName)        


class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Costumer(Person):
    def __init__(self,CreditCardNumbers):
        self.CreditCardNumbers = CreditCardNumbers
        
mehmet = Worker()
ali = Costumer()        
        
        
        
        
        
        
        
        
        
        
        
    