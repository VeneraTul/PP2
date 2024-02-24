import re

camel_str=input()


x = re.sub('(.)([A-Z][a-z]+)', r'\1 \2',camel_str )
y=re.sub('([a-z0-9])([A-Z])', r'\1 \2', x).lower()
z=re.sub(r"\s","_",y)

print(z)