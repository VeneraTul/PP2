import math

number=int(input("Input number of sides:" ))
length=int(input("Input the length of a side:" ))
Area=(number*(length**2)*(1/math.tan(math.pi/number)))/4
area=int(Area)
print("The area of the polygon is:",area)