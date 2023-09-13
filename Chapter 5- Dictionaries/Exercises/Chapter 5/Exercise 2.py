# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:55:56 2023

@author: Anzin R. Maglente
"""

"""
Create a glossary of the terms you learned from the previous lessons.
"""

glossary = {
    'string' : 'A sequence of characters that consist of letters, numbers, and symbols.',
    'input' : 'A funtion used to take an input from the user.',
    'reverse' : 'A method to invert the order of a given list.',
    'append' : 'A method to add an element to a given list.',
    'modulus' : 'A arithmetic operator that returns the reminder of a division.',
    }

print("My Glossary")

word = 'string'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'input'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'reverse'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'append'
print("\n\t" + word.title() + ": " + glossary[word])

word = 'modulus'
print("\n\t" + word.title() + ": " + glossary[word])