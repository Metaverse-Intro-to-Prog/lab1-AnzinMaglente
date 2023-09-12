# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:12:01 2023

@author: Anzin R. Maglente
"""

"""
Print date and time
"""

import datetime

now = datetime.datetime.now()

print ("Current date and time : ")

print (now.strftime("%Y-%m-%d %H:%M:%S"))