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

# Removing elements
int_array.remove(4)  # Remove an element
print("After removing:", int_array)

int_array = array.array('i', [2, 4, 6, 8, 10])

# Remove element at index 2 (removes 6)
int_array.pop(2)
print("After removing element at index 2:", int_array)

int_array = array.array('i', [2, 4, 6, 8, 10])

# Alternatively, we can use `del`
del int_array[1]  # Removes element at index 1 (2)
print("After using del to remove element at index 1:", int_array)

# Accessing elements
print("Element at index 1:", int_array[1])
