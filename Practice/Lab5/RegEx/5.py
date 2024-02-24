import re

word=input()

if re.search("^a.*?b$",word):
    print("Found")
else:
    print("Not Found")
