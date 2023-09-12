# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:50:20 2023

@author: Anzin R. Maglente
"""

"""
Stages of life, use a else-if chain to determine the person's age
"""

age = 70

if age < 2:
    print("you are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are a adult!")
else:
    print("You are a elder!")