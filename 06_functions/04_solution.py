# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.


import math

def circle_stats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circle_stats(5)
print(f"Area: {area}, Circumference: {circumference}") 