#booleans examples
a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))
print(bool(""))
print(bool(0))
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(None))
print(bool(False))

class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj))

def myfun():
    return True
print(bool(myfun()))
if myfun():
 print("Yes!")
else:
    print("No!")

x=200
print(isinstance(x,int))

#Operators examples
print(10+5)
print((6+3)-(6+3))
print(100+5*3)
print(5 + 4 - 7 + 3)


