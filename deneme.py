# -*- coding: utf-8 -*-

import sqlite3

def insertconnection():

    connection = sqlite3.connect("chinook.db")
    
    
    
def updateCostumer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""delete from CustomerId = 60 """
   
    connection.commit()
    connection.close()


deleteCostumer()    