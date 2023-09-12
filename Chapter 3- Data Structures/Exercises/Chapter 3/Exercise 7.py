# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:38:57 2023

@author: Anzin R. Maglente
"""

"""
Think of 5 places in the world you want to visit and do the following try out 
list sorting commands 
"""

Places = ["United Kingdom", "France", "Shibuya, Japan", "Venice, Italy", "Georgia"]
print("Original order:")
print (Places)
print("\nAlphabetical order:")
print (sorted(Places))
print("\nOriginal order:")
print (Places)
print("\nReverse Alphabetical order:")
print (sorted(Places, reverse = True))
print("\nOriginal order:")
print (Places)
print ("\nReversed order")
Places.reverse()
print (Places)
print ("\nOriginal order")
Places.reverse()
print (Places)
print ("\nAlphabetical order")
Places.sort()
print (Places)
print("\nReverse Alphabetical order:")
Places.sort(reverse = True)
print (Places)