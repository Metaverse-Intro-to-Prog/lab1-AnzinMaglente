# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:45:51 2023

@author: Anzin R. Maglente
"""

"""
Create a dictionary on major rivers and the where they flow through
Afterwards, print a sentence stating both variables, print another sentence
stating the river, and print another sentence stating the country 
"""

rivers = {
    'Cagayan River' : 'Philippines',
    'Godavari River' : 'India',
    'Loire River' : 'France',
    'Rochor River' : 'Singapore',
    'Murray River' : 'Australia',
    }

print ("Rivers and where they run through")

for river, country in rivers.items():
    print (f"\tThe {river.title()} flows through {country.title()}.")

print ("\nThe following rivers are included in the 'Rivers and where they run through' section:")
for river in rivers.keys():
    print (f"\t- {river.title()}")
    
print ("\nThe following countries are included in the 'Rivers and where they run through' section:")
for country in rivers.values():
    print (f"\t- {country.title()}")