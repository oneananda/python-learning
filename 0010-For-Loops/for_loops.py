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

for char in "Hello":
    print(char)

print()
print(f"{COMMENT} - finish")
print("======================================================")

COMMENT = "Iterating Over a Dictionary"

print(f"{COMMENT} - start")
print()

PERSON = {"name": "John", "age": 25, "city": "New York"}

for key, value in PERSON.items():
    print(key, ":", value)

print()
print(f"{COMMENT} - finish")
print("======================================================")

COMMENT = "Nested for Loop"

print(f"{COMMENT} - start")
print()

for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")

print()
print(f"{COMMENT} - finish")
print("======================================================")



