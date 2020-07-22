# -*- coding: utf-8 -*-

öğrenciler = ["ali","merve","hasan","mehmet"]

fileToAppend = open("öğrenciler.txt","a")

for öğrenci in öğrenciler:
    fileToAppend.write(öğrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()    