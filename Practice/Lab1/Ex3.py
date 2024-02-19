import random
print (random.randrange(1,10))
#
x=int(1)
y=int(2.8)
z=int("3")
y=float(1)
k=float(2.8)
w=float("3")
a=str("s1")
b=str(2)
c=str(3.0)

#
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#
a="Hello,World!"
print(a[1])
#
for x in "banana":
 print(x)
#
a="Hello,World!"
print(len(a))
#
txt="The best things in life are free!"
print("free" in txt)
if("free" in txt):
 print("Yes, 'free' is present.")
print("expensive" not in txt)
if("expensive" not in txt):
 print("No, 'expensive' is NOT present.")
 #
 b="Hello,World!"
 print(b[2:5])
 print(b[:5])
#
a=" Hello,World! "
print(a.strip())
print(a.upper())
print(a.lower())
print(a.replace("H","J"))
print(a.split())
#
age=36
txt="My name is John, and I am  {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
fsh="I want {} pieces of item {} for {} dollars"
print(fsh.format(quantity,itemno,price))
fsh="I want {0} pieces of item {2} for {1} dollars"
print(fsh.format(quantity,itemno,price))
#
txt = "We are the so-called \"Vikings\" from the north."
