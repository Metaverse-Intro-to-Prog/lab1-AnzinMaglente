# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:31:59 2023

@author: Anzin R. Maglente
"""

"""
T-shirt, make a function called "make_shirt" that accepts a size and message, print out the message
"""

def make_shirt (size, message):
    print (f"The size of the t-shirt will be: {size}")
    print (f'and it will have "{message}" written on it.\n')

make_shirt('medium', 'Hello world')
make_shirt(message="Hey! Python", size='large')