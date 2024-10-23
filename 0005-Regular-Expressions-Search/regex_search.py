"""
This program demonstrates the use of the re.search function in Python for regular expressions.
It checks for matches everywhere in the string.
"""

import re

# $ : Matches the end of a string
print('Searches for the word World! at the end of the string')

RESULT = re.search(r'World!$', 'Hello World!')
print(bool(RESULT))  # Output: True

print('Again searches for the word World! at the end of a different string')

RESULT = re.search(r'World!$', 'Hello World Welcome!')
print(bool(RESULT))  # Output: False

print('Searches for the word World! everywhere')

RESULT = re.search(r'World', 'Hello World Welcome!')
print(bool(RESULT))  # Output: True


