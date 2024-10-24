"""
This program demonstrates the use of the re.finditer function in Python for regular expressions.
It checks for all matches in the string.
"""
# regex_finditer.py

import re

PATTERN = r'\d+'

# String to search
TEXT = "I have 5 baskets and 10 lemons."

# Using finditer() to find all occurrences
MATCHES = re.finditer(PATTERN, TEXT)

# Loop through the matches and print details
for match in MATCHES:
    print(f"Found the number {match.group()} at position {match.start()} to {match.end()}")
