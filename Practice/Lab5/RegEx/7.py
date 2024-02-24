import re

snake_str=input()

x=re.sub("^[a-z]",lambda x: x.group(0).upper(),snake_str)
y=re.sub("_[a-z]",lambda x: x.group(0)[1].upper(),x)

y=y.replace("_","")

print(y)