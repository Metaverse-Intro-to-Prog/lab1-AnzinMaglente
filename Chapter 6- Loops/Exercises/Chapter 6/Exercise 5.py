# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:07:27 2023

@author: Anzin R. Maglente
"""

"""
Deli, make a list titled "sandwich_orders", fill it with various sandwiches, make another list 
titled "finished_sandwiches", this will be empty. Print a message that it would be prepared, 
but there is no more Pastrami, make sure it doesn't go to finished sandwiches and it has to appear
at least three times in the list'
"""

sandwich_orders = ["Pastrami", "Club", "Tuna", "Turkey", "Pastrami", "Roast Beef", "Grilled Cheese", "Pastrami"]
finished_sandwiches = []

print ("""Hello! Welcome to Subway what would you like?

...

Oh sorry, we ran out of pastrami, but we are able to fulfill your other orders\n""")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    cooking_sandwich = sandwich_orders.pop()
    print(f"your {cooking_sandwich} sandwich is currently being prepared, please wait for a moment.")
    finished_sandwiches.append(cooking_sandwich)

print ("\nALright it is done, here is your order!\n")
for sandwich in finished_sandwiches:
    print(f"\tI made an {sandwich} sandwich for you")