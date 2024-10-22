# 0004-regex-match.py

import re

result = re.match(r'Hello', 'Hello World')
print(bool(result))  # Output: True

# No Match if Not at the Beginning

result = re.match(r'World', 'Hello World')
print(bool(result))  # Output: False



