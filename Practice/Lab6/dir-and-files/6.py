import os

for i in range(ord('A'),ord('Z')+1):
    file=open(f"{chr(i)}.txt",'a')

    file.close()



