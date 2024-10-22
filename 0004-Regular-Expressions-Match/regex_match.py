"""
This program demonstrates the use of the re.match function in Python for regular expressions.
It checks for matches at the beginning of the string.
"""

# regex_match.py

import re

# Match at the beginning of the string
print('Match at the beginning of the string wity Hello')
RESULT = re.match(r'Hello', 'Hello World')
print(bool(RESULT))  # Output: True

# No Match if not at the beginning of the string
print('No Match if not at the beginning of the string with World')
RESULT = re.match(r'World', 'Hello World')
print(bool(RESULT))  # Output: False

# Using ^ to Match the Start
print('Using ^ to Match the Start')
print('Checking if the word starts with H')
RESULT = re.match(r'^H', 'Hello World')
print(bool(RESULT))  # Output: True

print('Checking if the word starts with He')
RESULT = re.match(r'^He', 'Hello World')
print(bool(RESULT))  # Output: True

print('Checking if the word starts with Hi')
RESULT = re.match(r'^Hi', 'Hello World')
print(bool(RESULT))  # Output: False
