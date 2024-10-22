# 0003-regex-findall.py

This script demonstrates the use of Python's `re.findall()` function to find all words in a given text that start with the letter "I".

## Description
The script imports the `re` module (Python's regular expressions module) and uses `re.findall()` with the pattern `\bI\w+` to find all words that begin with the capital letter "I".

- `\b` asserts a word boundary, ensuring we only match words starting with "I".
- `I` matches the literal capital letter "I".
- `\w+` matches one or more word characters following "I".

The script runs two examples to demonstrate the regex:

1. Text: "The rain is happening in India"
   - Expected output: `["India"]`

2. Text: "The rain is happening in India and Ireland"
   - Expected output: `["India", "Ireland"]`

## Usage
To run the script, you need Python 3 installed on your system. You can execute it using the following command:

```bash
python 0003-regex-findall.py
```

## Example Output
```
['India']
['India', 'Ireland']
```

## Dependencies
- Python 3.x
- `re` module (comes built-in with Python)

