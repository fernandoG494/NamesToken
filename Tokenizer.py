# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:32:51 2021

@author: Fernando
"""

with open('NamesFiles/Draconic.txt', 'r') as f:
    data = f.read()

split_data = data.split(",");

outF = open('Generated/Draconic.txt', "w")
writeF = open('Generated/Draconic.txt', "a")

for data in split_data:
    writeF.write(data + "\n")
    
writeF.close()

f = open("Generated/Draconic.txt", "r")
print(f.read())