# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:29:27 2023

@author: Anzin R. Maglente
"""

"""
Make a list of people you would want to invite over for dinner and print out
a message for them, inviting them over. However one person couldn't attend, and
thus, the list was changed.
"""

Invitees = ["Lianne", "Carl", "Elex", "Kent", "Aki"]
for i in Invitees:
    print ("Dear " + i.title() + """.
           You have been cordinally invited to my house for dinner, 
           please respond as soon as possible, thank you\n""")

print("However, " + Invitees[0] + " is unable to come, so a new list was made\n")
del Invitees[0]
Invitees.append("Fadi")
for i in Invitees:
    print ("Dear " + i.title() + """,
           You have been cordinally invited to my house for dinner, 
           please respond as soon as possible, thank you\n""")