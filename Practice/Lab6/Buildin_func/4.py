
from time import sleep
import math
num=int(input())
milsec=int(input())
sleep(milsec/1000)
square=math.sqrt(num)
print(f"Square root of after {milsec} miliseconds is {square}")


#цифры должны вводится с новой строки