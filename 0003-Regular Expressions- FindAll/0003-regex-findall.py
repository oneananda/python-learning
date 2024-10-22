# 0003-regex-findall.py

import re
text = "The rain in happening in India"
result = re.findall(r"\bI\w+", text)
print(result)

text = "The rain in happening in India and Ireland"
result = re.findall(r"\bI\w+", text)
print(result)