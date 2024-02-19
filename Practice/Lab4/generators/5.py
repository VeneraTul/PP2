def decreasing(n):
        i=n
        while i>=0:
            yield i
            i-=1

n=int(input())
print(list(decreasing(n)))
    