# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:32:51 2021

@author: Fernando
"""

dictionary = 'Dark_elven.txt'

with open('NamesFiles/' + dictionary, 'r') as f:
    data = f.read()

split_data = data.split(",");

outF = open('Generated/'  + dictionary, "w")
writeF = open('Generated/' + dictionary, "a")

for data in split_data:
    writeF.write(data + "\n")
    
writeF.close()

f = open("Generated/" + dictionary, "r")
print(f.read())