"""
This program demonstrates the use of the arrays in Python.
"""
# array_functions.py

import array

# Create an integer array

int_array = array.array('i', [2, 4, 6, 8, 10])
print(int_array)

# Basic operations on array

# Adding elements
int_array.append(12)  # Append an element

print("After appending:", int_array)