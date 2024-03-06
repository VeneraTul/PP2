import os
list1=list(map(str,input().split()))
file=open("list_ex","w")

file.write(str(list1))
file.close()

