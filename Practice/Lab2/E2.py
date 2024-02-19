#Lists examples
thislists=["apple", "banana", "cherry"]
print(thislists)

print(len(thislists))

print(thislists[1])

print(thislists[-1])

if "apple" in thislists:
    print("Yes, 'apple' is in the fruits list")

thislist=["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

list1=["apple","banana","cherry"]
list2=[1, 5, 7, 9, 3]
list3=[True,False,False]

list4=["abc", 34, True, 40, "male"]
print(type(list4))

thislist = list(("apple", "banana", "cherry")) 
print(thislist)

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
print(thislist2[:4])
print(thislist2[2:])
print(thislist2[-4:-1])

thislist1=["apple", "banana", "cherry"]
thislist1[1]="blackcurrant"
print(thislist1)

thislists1=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislists1[1:3]=["blackcurrant", "watermelon"]
print(thislists1)

thislist3=["apple", "banana", "cherry"]
thislist3[1:2]=["blackcurrant", "watermelon"]
print(thislist3)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist.append("orange")
print(thislist)
thislist.insert(1,"kiwi")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist4 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist4.extend(thistuple)
print(thislist4)

thislist4.insert(3,"banana")
print(thislist4)

thislist4.remove("banana")
print(thislist4)

thislist4.pop(1)
print(thislist4)

thislist4.pop()
print(thislist4)

del thislist4[0]
print(thislist4)

thislist4.clear()
print(thislist4)

del thislist4



