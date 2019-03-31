#To find the Volume of a frustum of a cone

import math
h=input("Enter the height of the frustum:")
R=input("Enter the bigger radius of the frustum:")
r=input("Enter the smaller radius of the frustum:")

V= 22*h*(R**2+r**2+R*r) / (3*7) 

print "The Volume of the frustum is:",V
