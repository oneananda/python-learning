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

print('. : Matches any character except newline')

RESULT = re.search(r'W.rld', 'World')
print(bool(RESULT))  # Output: True

RESULT = re.search(r'W.rld', 'Worlds')
print(bool(RESULT))  # Output: True

RESULT = re.search(r'W.rld', 'Worrlds')
print(bool(RESULT))  # Output: False

print('* : Matches 0 or more repetitions of the preceding pattern')

RESULT = re.search(r'ab*', 'a')
print(bool(RESULT))  # Output: True

# Pattern r'ab*':
# The regular expression ab* is interpreted as:
# 'a': Match the character 'a'.
# 'b*': Match zero or more occurrences of the character 'b'.
# This means the pattern will match an 'a' followed by zero or more 'b' characters.


RESULT = re.search(r'ab*', 'b')
print(bool(RESULT))  # Output: False

print('{} : Matches exactly the specified number of repetitions')

RESULT = re.search(r'a{3}', 'aaa')
print(bool(RESULT))  # Output: True

RESULT = re.search(r'a{3}', 'aaaa')
print(bool(RESULT))  # Output: True

RESULT = re.search(r'a{3}', 'aab')
print(bool(RESULT))  # Output: False

print('[] : Matches any one character within the brackets')

RESULT = re.search(r'[abc]', 'apple')
print(bool(RESULT))  # Output: True

RESULT = re.search(r'[abc]', 'xyz')
print(bool(RESULT))  # Output: False

print('| : Acts like an OR (matches one of the alternatives)')

RESULT = re.search(r'cat|dog|parrot', 'I have a cat')
print(bool(RESULT))  # Output: True

RESULT = re.search(r'cat|dog|parrot', 'I have a zebra')
print(bool(RESULT))  # Output: False
