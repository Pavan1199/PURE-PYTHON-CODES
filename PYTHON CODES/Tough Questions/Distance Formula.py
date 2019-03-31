#To use the distance formula to find the distance between two points in the cooridnate system

import math 
x1=input("Enter the value of x1:")
x2=input("Enter the value of x2:")
y1=input("Enter the value of y1:")
y2=input("Enter the value of y2:")

a = (x2-x1)**2 + (y2-y1)**2

a=math.sqrt(a) 

print "The distance between the points A and B is:",a
