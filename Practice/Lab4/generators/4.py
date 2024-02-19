def squares(a,b):
    for i in range(a,b+1):
        yield i*i

a=int(input())
b=int(input())
for num in squares(a,b):
    print(num,end=" ")
