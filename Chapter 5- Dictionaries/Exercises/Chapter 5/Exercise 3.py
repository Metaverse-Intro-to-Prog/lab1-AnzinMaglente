# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:55:56 2023

@author: Anzin R. Maglente
"""

"""
Create a glossary of the terms you learned from the previous lessons. Now with
the use of looping.
"""

glossary = {
    'string' : 'A sequence of characters that consist of letters, numbers, and symbols.',
    'input' : 'A funtion used to take an input from the user.',
    'reverse' : 'A method to invert the order of a given list.',
    'append' : 'A method to add an element to a given list.',
    'modulus' : 'A arithmetic operator that returns the reminder of a division.',
    'float' : 'A data type that returns a number with a decimal point.',
    '"if" statement' : 'A statement that whether or not a condition is met.',
    'list' : 'A data structure that stores different kinds of values',
    'strip' : 'A function that removes white space from both sides of a statement',
    'comment' : 'A line of text that appears within console that does not affect the output',
    }

print("My Glossary")
for word, definition in glossary.items():
    print("\n\t" + word.title() + ": " + definition)
