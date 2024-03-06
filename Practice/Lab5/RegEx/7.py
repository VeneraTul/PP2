import re
word = input()
li = []
reg6 = re.split("_", word)
for x in reg6:
    li.append(x)
for y in li:
    print(y.capitalize() , end="")