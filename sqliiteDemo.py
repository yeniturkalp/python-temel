# -*- coding: utf-8 -*-

import sqlite3

def insertoperasyonları():

    connection = sqlite3.connect("chinook.db")
    
    
#    cursor = connection.execute("""select FirstName, Lastname from customers
#                               where country = 'Brazil' or country = 'Canada' 
#                               order by FirstName,LastName desc """)
#    
#    for row in cursor:    
#        print("FirstName = "+ row[0])
#        print("LastName = "+ row[1])
#        print("********************")
#    
#    
#    cursor = connection.execute(""" select city ,count(*) from Customers group by city 
#                                having count(*)>1 order by  count(*) desc """)
#    
#    for row in cursor:    
#        print(" city = "+ row[0])
#        print("count = "+ str(row[1]))
#        print("********************")
    
    
    cursor = connection.execute("""select FirstName, Lastname from customers
                               where FirstName like 'ja%' """)
    
    for row in cursor:    
        print("FirstName = "+ row[0])
        print("LastName = "+ row[1])
        print("********************")
        
        
        connection.close()
#        
#        
insertconnection()

def inserCostumer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into 
                       customers(FirstName,LastName,city,Email)
                       values('alp','yenitürk','bayburt',
                       'alperw@gmail.com') """)
    connection.commit()
    connection.close()


#inserCostumer()    



def updateCostumer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city 'bursa'
                       where city 'bayburt'"""
   
    connection.commit()
    connection.close()

#updateCostumer()        
 


def updateCostumer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from CustomerId = 60 """
   
    connection.commit()
    connection.close()


#deleteCostumer()

def joinoperasyonları():

    connection = sqlite3.connect("chinook.db")

    cursor = connection.execute("""select artists.Name , albums.Title  from artists
                                  inner join albumson 
                                  artists.ArtistId = albums.ArtistId""")
    
    for row in cursor:    
        print("Name = "+ row[0] + "Tittle =" + row[1])
       
        print("********************")
    connection.close()         

joinconnection()















       