"""
This program demonstrates the use of the NumPy arrays in Python.
"""

# array_numpy.py

import numpy as np

NUMPY_ARRAY = np.array([2, 4, 6, 8, 10])
print("NumPy array:", NUMPY_ARRAY)

# Adding elements - create a new array
NEW_ARRAY = np.append(NUMPY_ARRAY, 6)
print("After appending:", NEW_ARRAY)

# Removing elements - create a new array without the specific element
NEW_ARRAY = np.delete(NUMPY_ARRAY, 2)  # Deletes element at index 2 and add the result
print("After removing:", NEW_ARRAY)
