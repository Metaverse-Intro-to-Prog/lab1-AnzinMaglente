# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:38:52 2023

@author: Anzin R. Maglente
"""

"""
Print your name with some white spaces and use the three strips: lstrip(), rstrip(), and strip().
"""

Name = " Anzin Maglente "
Name_remove_leading = Name.lstrip()
Name_remove_trailing = Name.rstrip()
Name_remove_both = Name.strip()
print ("My name:\n\t_" + Name + "_\nMy name without the leading white space:\n\t" + "_" + Name_remove_leading + "_\nMy name without the trailing white space\n\t" + Name_remove_trailing + "_\nMy name without both white spaces\n\t_" + Name_remove_both + "_")