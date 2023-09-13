# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:49:46 2023

@author: Anzin R. Maglente
"""

"""
Cities, make a function called "describe_city" wherein it accepts a city and a country, let it print a 
simple sentence and call the function three times (one is not with the default country)
"""

def describe_city(city="Dubai", country="United Arab Emirates"):
    print (f"{city} is located in {country}")

describe_city()
describe_city(city="Toronto", country="Canada")
describe_city(city="Abu Dhabi")