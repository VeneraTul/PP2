#tuple examples
thistuple=('apple','orange','banana')
print(thistuple)
print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

ttuple1=('apple',)
print(type(ttuple1)) #tuple
ttuple2=('apple')
print(type(ttuple2)) #str

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

x=('apple','orange','banana')
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

thistuple=('apple','orange','banana')
y=list(thistuple)
y.append("melon")
thistuple=tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

x=('apple','orange','banana')
y=list(x)
y.remove("apple")
x=tuple(y)
print(x)

del thistuple

fruits=('apple','banana','cherry')
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

tthis=('apple','banana','cherry')
for x in tthis:
    print(x)
for i in range(len(tthis)):
    print(tthis[i])

ttis=('apple','banana','cherry')
i=0
while i<len(ttis):
    print(ttis[i])
    i+=1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
mytuple=tuple1 *2
print(mytuple)



