# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:57:06 2023

@author: Anzin R. Maglente
"""

"""
Pizza Topping, write a prompt asking for toppings on pizza until the user writes 'quit'
for each topping, print out that you will add it to the pizza
 
"""

print ("""Hello, welcome to Pizza Time! What would you want on your pizza?
If you want to exit out of this program please write 'quit'""")

while True:
    topping = input("\nWhat toppings would you like for your pizza?\n\t")
    if topping != 'quit':
        print ("\nI'll add " + topping + " on to your pizza!")
    else:
        break