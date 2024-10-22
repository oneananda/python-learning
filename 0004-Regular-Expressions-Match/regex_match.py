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

print('Matching Digits at the Start')
RESULT = re.match(r'\d+', '1234abc')
print(RESULT.group())  # Output: '1234'

print('Matching Digits at the Start')
RESULT = re.match(r'[A-Za-z]+', 'PythonIsGreat123')
print(RESULT.group())  # Output: 'PythonIsGreat'

print('Matching Digits at the Start with spaces')
RESULT = re.match(r'[A-Za-z]+', 'Python Is Great123')
print(RESULT.group())  # Output: 'Python', Reason : Space is not part of [A-Za-z].

print('Case-Insensitive Matching')
RESULT = re.match(r'hello', 'Hello World', re.IGNORECASE)
print(bool(RESULT))  # Output: True

print('Matching with Quantifiers')
RESULT = re.match(r'\w{6}', 'abcde12345')
print(RESULT.group())  # Output: 'abcde1'

print('Matching with Optional Characters (?)')
RESULT = re.match(r'colou?r', 'color')
print(RESULT.group())  # Output: True

print('Matching Alphanumeric Strings')
RESULT = re.match(r'[A-Za-z0-9]+', 'Python123!')
print(RESULT.group())  # Output: Python123
