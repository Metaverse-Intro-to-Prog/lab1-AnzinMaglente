# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:41:54 2023

@author: Anzin R. Maglente
"""

"""
Deli, make a list titled "sandwich_orders", fill it with various sandwiches, make another list 
titled "finished_sandwiches", this will be empty. Print a message that it would be prepared, 
"""

sandwich_orders = ["Pastrami", "Club", "Tuna", "Turkey", "Grilled cheese"]
finished_sandwiches = []

print ("""Hello! Welcome to Subway what would you like?

...

Okay, right away!\n""")

while sandwich_orders:
    cooking_sandwich = sandwich_orders.pop()
    print(f"your {cooking_sandwich} sandwich is currently being prepared, please wait for a moment.")
    finished_sandwiches.append(cooking_sandwich)

print ("\nALright it is done, here is your order!\n")
for sandwich in finished_sandwiches:
    print(f"\tI made an {sandwich} sandwich for you")