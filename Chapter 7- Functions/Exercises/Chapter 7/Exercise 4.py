# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:31:59 2023

@author: Anzin R. Maglente
"""

"""
T-shirt, make a function called "make_shirt" that accepts a size and message, print out the message
now make size default to "large" and message should default to "I love Python". Test it out using
three examples, one: a large shirt with the default message, one medium shirt with the default
message, and lastly, any size with any message
"""

def make_shirt (size='large', message='I love Python'):
    print (f"The size of the t-shirt will be: {size}")
    print (f'and it will have "{message}" written on it.\n')

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='The best t-shirt around!')