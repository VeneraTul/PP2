import os
path=input()

if os.path.exists(path)==True:
    os.remove(path)
else:
    print("Path doesn't exist")