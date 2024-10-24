# regex_finditer.py

## Overview

This Python program demonstrates the use of the `re.finditer()` function to perform pattern matching using regular expressions. It searches for all occurrences of numbers in a given string and prints the found matches along with their positions in the string.

## Features

- Utilizes Python's `re` module for regular expressions.
- Finds and prints all occurrences of numbers (one or more digits) in the given text.
- Provides details such as the matched numbers and their starting and ending positions in the string.


This Python program demonstrates how to use the `re.finditer()` function from the `re` (regular expression) module to find all occurrences of a pattern in a given string.

### Breakdown of the code:

1. **Define the Text to Search**:
   - `TEXT = "I have 5 baskets and 10 lemons."`: This is the text string where the pattern (in this case, digits) will be searched.

2. **Use of `re.finditer()`**:
   - `MATCHES = re.finditer(PATTERN, TEXT)`: This function searches the `TEXT` for all occurrences of the pattern specified by `PATTERN`. The `finditer()` function returns an iterator of match objects, which contain information about the match (such as the start and end position of the match in the string).
   
   - The benefit of using `finditer()` over other functions (like `findall()`) is that it returns an iterator of `match` objects, allowing for detailed access to the match (positions, groups, etc.).

3. **Looping Through Matches**:
   - The `for` loop iterates through all the match objects returned by `finditer()`. For each match:
     - `match.group()` retrieves the matched text (in this case, the digits found).
     - `match.start()` returns the starting index of the match.
     - `match.end()` returns the ending index of the match (exclusive).
     - The program prints the matched digits and their positions in the string.

### Output:
For the input string `"I have 5 baskets and 10 lemons."`, the program will find two matches for the digits: `5` and `10`.

The output will be:
```
Found the number 5 at position 7 to 8
Found the number 10 at position 20 to 22
```

This shows the matched numbers and their corresponding positions in the string.

