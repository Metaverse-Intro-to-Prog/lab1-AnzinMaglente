# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:20:24 2023

@author: Anzin R. Maglente
"""

"""
Movie Tickets, make a loop function wherein the cost of a ticket depends on the
age of the person 
"""

movie_prompt = "\nHow old are you?"
movie_prompt += "\nEnter 'quit' if you are finished.\n\t"

while True:
    age =  input(movie_prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print ("\nFor you the ticket is free.")
    elif age < 13:
        print ("\nThat will be $10.")
    else:
        print ("\nThat will be $15.")