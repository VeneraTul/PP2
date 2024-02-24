import re

word=input()

x=re.sub(r"([A-Z][a-z]+)",r" \1",word).strip()

print(x)