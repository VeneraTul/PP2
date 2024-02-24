import re

word=input()

matches=re.findall("ab*",word)

if matches:
    print("It is found")
else:
    print("Not found")