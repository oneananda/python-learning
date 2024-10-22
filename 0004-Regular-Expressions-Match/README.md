# Regex Match Demo in Python

### regex_match.py

This program demonstrates the use of the `re.match()` function in Python to perform pattern matching at the beginning of a string using regular expressions (regex). It provides multiple examples showing how `re.match` behaves under various scenarios such as matching characters, digits, case-insensitive strings, and more.

## Examples Covered

The program covers the following use cases:

1. **Basic Matching**:
    - Check if the string starts with "Hello".
    
    ```python
    re.match(r'Hello', 'Hello World')
    ```

2. **No Match if Not at the Beginning**:
    - Check for "World" at the start of the string, which fails because "Hello" comes first.
    
    ```python
    re.match(r'World', 'Hello World')
    ```

3. **Using `^` to Enforce Start of String**:
    - Match strings that start with specific characters like "H" or "He".

    ```python
    re.match(r'^H', 'Hello World')
    ```

4. **Matching Digits at the Start**:
    - Find one or more digits at the beginning of the string.

    ```python
    re.match(r'\d+', '1234abc')
    ```

5. **Matching Alphanumeric Strings**:
    - Match alphanumeric sequences such as "PythonIsGreat123".

    ```python
    re.match(r'[A-Za-z]+', 'PythonIsGreat123')
    ```

6. **Case-Insensitive Matching**:
    - Ignore case when matching "hello" against "Hello World".

    ```python
    re.match(r'hello', 'Hello World', re.IGNORECASE)
    ```

7. **Using Quantifiers**:
    - Match a specific number of characters using `{}` quantifiers.

    ```python
    re.match(r'\w{6}', 'abcde12345')
    ```

8. **Optional Characters (`?`)**:
    - Match both "color" and "colour" using an optional character `u`.

    ```python
    re.match(r'colou?r', 'color')
    ```

9. **Matching Alphanumeric Strings and Special Characters**:
    - Match alphanumeric strings and note that special characters are excluded.

    ```python
    re.match(r'[A-Za-z0-9]+', 'Python123!')
    ```

## Output

Each example prints the result of the regex match as `True` or `False`, or prints the matched substring when applicable.

For example:
```bash
Match at the beginning of the string wity Hello
True
No Match if not at the beginning of the string with World
False
Using ^ to Match the Start
Checking if the word starts with H
True
Checking if the word starts with He
True
Checking if the word starts with Hi
False
...
```


---




