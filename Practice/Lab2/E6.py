#Dictionaries
thisdict={"brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 }
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict=dict(name="John",age = 36, country = "Norway")
print(thisdict)
x=thisdict.get("age")
print(x)
y=thisdict.keys()
print(y)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
t = car.values()
print(x)
print(t)
car["color"] = "white"
e=car.items()
print(x) 
print(t)
print(e)
if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color":"red"})
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["brand"]
print(thisdict)
#del thisdict
#thisdict.clear()

thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict2:
  print(x)

for y in thisdict2:
  print(thisdict2[y])

for z in thisdict2.values():
  print(z)
for j in thisdict2.keys():
  print(j)

for a,b in thisdict2.items():
  print(a,b)
#
  

  tthisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict=tthisdict.copy()
print(mydict)
yourdict=dict(tthisdict)
print(yourdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print(myfamily["child2"]["name"])
