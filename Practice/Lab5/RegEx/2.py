import re

word=input()

matches=re.findall("ab{2,3}",word)

print(matches)
