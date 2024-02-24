import re

sentence=input()

x=re.sub(r"\s",":",sentence)
y=re.sub(r"\.",":",x)
z=re.sub(r",",":",y)

print(z)
