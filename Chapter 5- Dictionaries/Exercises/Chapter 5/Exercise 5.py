# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:13:54 2023

@author: Anzin R. Maglente
"""

"""
Create several dictionaries containing information of a pet, this will include 
it's owner, and the kind of animal
"""

pets = []

pet = {
       'Name' : 'Pusa',
       'Owner' : 'Anzin',
       'Kind of animal' : 'British Shorthair Persian Cat',
       'Age' : '12 years old',
       'Gender' : 'Male'}

pets.append(pet)

pet = {
       'Name' : 'Mitski',
       'Owner' : 'Andrea',
       'Kind of animal' : 'Corgi Dog',
       'Age' : '1 year old',
       'Gender' : 'Female'}
pets.append(pet)

pet = {
       'Name' : 'Smokey',
       'Owner' : 'Fadi',
       'Kind of animal' : 'American Shorthair Persian Cat',
       'Age' : '4 years old',
       'Gender' : 'Male'}
pets.append(pet)

for pet in pets:
    print(f"\n{pet['Name'].title()} Data:")
    for key, value in pet.items():
        print(f"\t{key} : {value}")