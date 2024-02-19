#examples of lists
thislist=["apple","cherry","banana"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
[print(x) for x in thislist ]

thislist1=["apple","cherry","banana"]
i=0
while i<len(thislist1):
    print(thislist1[i])
    i=i+1

fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
newlist1=[x for x in fruits if "a" in x]
newlist2=[x for x in fruits if x!="apple"]
newlist3=[x for x in fruits]
newlist4=[x for x in range(10)]
newlist5=[x for x in range(10) if x<5]
newlist6=[x.upper() for x in fruits]
newlist7=['hello' for x in fruits]
newlist8=[x if x!="apple" else "orange" for x in fruits]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
print(newlist1)
print(newlist2)
print(newlist3)
print(newlist4)
print(newlist5)
print(newlist6)
print(newlist7)
print(newlist8)

thislist9=["apple","cherry","banana"]
thislist9.sort()
print(thislist9)
thislist9.sort(reverse=True)
print(thislist9)

thislis = [100, 50, 65, 82, 23]
thislis.sort()
print(thislis)
thislis = [100, 50, 65, 82, 23]
thislis.sort(reverse=True)
print(thislis)

def myfun(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfun)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
thislist.reverse()
print(thislist)

thislist=['apple','orange','cherry']
mylist=thislist.copy()
mylist1=list(thislist)
print(mylist)
print(mylist1)

list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)
for x in list2:
    list1.append(x)
print(list1)

list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)
