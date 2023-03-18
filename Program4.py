'''
Write a program to input radius of a circle and show its circumference and area 
of that circle.
Hint=use formula 2*pi*r and pi*r*r
'''
import math
print("Enter radius of circle")
r=float(input())
circumference=2*math.pi*r
print("Circumference is",circumference)
area=math.pi*r*r
print("Area is",area)
