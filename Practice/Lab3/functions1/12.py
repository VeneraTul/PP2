def histogram(numbers):
    for i in numbers:
        for j in range(i):
            print("*" , end = "")
        print()
histogram([4, 9 ,7])
