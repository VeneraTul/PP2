import re

word=input()

x=re.split(r"(?=[A-Z])",word)

print(x)