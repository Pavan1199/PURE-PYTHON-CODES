#program to find the area of a triangle if all 3 sides are given
import math
a=input ('enter first side:')
b=input ('enter second side:')
c=input ('enter third side:')
s=(a+b+c)/2.0
print 'semi-perimeter=',s
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print 'area=',area
