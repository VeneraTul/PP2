import re

text=input()

matches=re.findall("[A-Z][a-z]+",text)

print(matches)