# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:52:55 2023

@author: Anzin R. Maglente
"""

"""
Create a list function of some of your friends and print it a message with their personal names
"""

my_friends = ["Cid", "James", "Ericka", "Lianne", "Carl"]
message = ("Hello, how are you today ")

for i in my_friends:
    print(message + i.title() + "?")