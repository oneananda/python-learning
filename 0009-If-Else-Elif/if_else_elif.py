"""
This program demonstrates the use of the if_else_elif in Python.
"""

# if_else_elif.py

AGE = 40

print(f"If-example")
AGE = 18
if AGE >= 18:
    print("You are eligible to vote.")

print(f"======================================================")


print(f"If-else-example")
print(f"Hospital admission when the age is {AGE}")

if AGE <= 18:
    print("You should be admitted to the Pediatric Department.")
else:
    print("You should be admitted to the Adult Department.")
print(f"======================================================")

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
