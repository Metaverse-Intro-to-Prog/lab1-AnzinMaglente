# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:29:27 2023

@author: Anzin R. Maglente
"""

"""
Make a list of people you would want to invite over for dinner and print out
a message for them, inviting them over. However one person couldn't attend, and
thus, the list was changed. The list was once again altered this time, you can
only have 2 people who you could invite
"""

Invitees = ["Lianne", "Carl", "Elex", "Kent", "Aki"]
for i in Invitees:
    print ("Dear " + i.title() + """.
           You have been cordinally invited to my house for dinner, 
           please respond as soon as possible, thank you\n""")

print("However, " + Invitees[0] + " is unable to come, so a new list was made\n")
Invitees.pop(0)
Invitees.append("Fadi")
for i in Invitees:
    print ("Dear " + i.title() + """,
           You have been cordinally invited to my house for dinner, 
           please respond as soon as possible, thank you\n""")
           
print("""That was until I realized that I could have only invited two people
      (cause the house ain't that big), and so I had to send out a message to the following:""")

Invitees.pop(0)
Invitees.pop(2)
Invitees.pop(1)
Sorry = ["Carl", "Kent", "Aki"]

for i in Sorry:
    print("Dear " + i.title() + """,
          I sadly have to inform you that you are no longer invited to dinner,
          due to some unforeseen circumstances, I hope you understand.
          """)

print("And all that remained was two, " + Invitees[0] + " and " + Invitees[1] + "\n")

for i in Invitees:
    print("Dear " + i.title() + """,
          You are still invited to dinner, please don't forget. This is just a
          reminder, thank you in advance.
          """)

del Invitees #I tried printing Invitees after this, it showed up as an error
