"""
This program demonstrates the use of the for loops in Python.
"""

# for_loops.py

print("For loops example")
print()

COMMENT = "Iterating Over a List"
print(f"{COMMENT} - start")
print()

FRUITS = ["banana", "apple", "orange"]

for fruit in FRUITS:
    print(fruit)

print()
print(f"{COMMENT} - finish")
print("======================================================")

COMMENT = "Using range() to Iterate Over Numbers"
print(f"{COMMENT} - start")
print()

for i in range(10):
    print(i) # Print 10 numbers starting from 0 (0-9)

print()
print(f"{COMMENT} - finish")
print("======================================================")

COMMENT = "Iterating Over a String"

print(f"{COMMENT} - start")
print()

for i in range(10):
    print(i) # Print 10 numbers starting from 0 (0-9)

print()
print(f"{COMMENT} - finish")
print("======================================================")
