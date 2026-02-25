# % = remainder/modules sign
# ** = exponentiation sign: multiply a no by itself a certain amount of times

# BUILT_IN FUNCTIONS

x = 3.14
y = 4
z = 5


# ROUND(to a whole no)
result = round(x)
# Absolute (how far it is from zero without caring if its pstv or ngtv)
result = abs(y)
# Power = (needs base and exponate, multiply no certain times)
result = pow(6,3)
# Max & Min(find the highest and lowest value)
result = max(x,y,z)
result = min(x,y,z)
print(result)


# Constant functions

import math

x= 11.5
print(math.pi)
print(math.e)
# Find square root
result = math.sqrt(x)
# Ceiling fnctn( rounds a number up to nearest whole number)
result = math.ceil(x)
# Floor (rounds to nearest whole number down)
result = math.floor(x)
print(result)


# Exercise
# 1: Circumference of a circle = (2 * pi * radius)

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)} cm")


# 2: Area of a circle(pi * radius^2)

radius = float(input("Enter the radius of the circle: "))
area = math.pi *  pow(radius,2)
print(f"The area is: {round(area,2)} cm^2")


# 3: Hypotenuse of triangle

radius = float(input("Enter the radius of the circle: "))
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c= math.sqrt(pow(a,2) + pow(b, 2))
print(f"side c = {c}")


# 4: Area of a rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area is: {round(area,2)} cm^2")

