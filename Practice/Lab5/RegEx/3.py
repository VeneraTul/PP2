import re

text=input()

matches=re.findall("[a-z]+_[a-z]+",text)

print(matches)
    