"""
This program contains functions for performing regular expressions on strings.
"""

# regex_findall.py

import re
TEXT = "The rain in happening in India"
RESULT = re.findall(r"\bI\w+", TEXT)
print(RESULT)

text = "The rain in happening in India and Ireland"
RESULT = re.findall(r"\bI\w+", TEXT)
print(RESULT)
