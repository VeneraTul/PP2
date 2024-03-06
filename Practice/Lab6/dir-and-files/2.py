import os
path="C:\\Users\\Венера"

print(os.access(path,os.F_OK))
print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))