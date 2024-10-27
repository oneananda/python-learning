"""
This program demonstrates the use of the if_else_elif in Python.
"""

# if_else_elif.py

AGE = 40

print("If-example")
AGE = 18
if AGE >= 18:
    print("You are eligible to vote.")

print("======================================================")
print()

print("If-else-example")
print("Hospital admission when the age is {AGE}")

if AGE <= 18:
    print("You should be admitted to the Pediatric Department.")
else:
    print("You should be admitted to the Adult Department.")
print(f"======================================================")
print()

print("If-else-with-multiple-lines-example")
print(f"Hospital admission when the age is {AGE}")

if AGE <= 18:
    print(f"Your age is {AGE}.")
    print("You should be admitted to the Pediatric Department.")
else:
    print(f"Your age is {AGE}.")
    print("You should be admitted to the Adult Department.")
print("======================================================")
print()

print("if-elif-else example")
print("elif = else if")

MARKS = 85
if MARKS >= 90:
    print("Grade: A")
elif MARKS >= 75:
    print("Grade: B")
elif MARKS >= 60:
    print("Grade: C")
else:
    print("Grade: D")
print(f"======================================================")
print()

print("Nested if Statements example")

NUMBER = 15
if NUMBER > 0:
    if NUMBER % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")

print(f"======================================================")
print()

print("Using Logical Operators example")

AGE = 40

has_id = True

if AGE >= 18 and has_id:
    print("You can enter the club, as your age is {AGE}.")
else:
    print("Entry denied, as your age is {AGE}.")


print("======================================================")
