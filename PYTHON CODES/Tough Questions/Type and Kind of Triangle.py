# Program to find the

import math


a=input("Enter the first side:")
b=input("Enter the second side:")
c=input("Enter the third side:")

if a+b>c or a+c>b or b+c>a:
   print "The given sides form a triangle:"
   if a==b==c:
       print "The triangle is an equilateral triangle:"
   elif a==b or b==c or a==c:
       print "The triangle is an isoceles triangle:"
   else:
       print "The triangle is a scalene triangle:"
   if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
       print "The triangle is a right angled triangle:"

   s=(a+b+c)/2
   v=math.sqrt(s*(s-a)*(s-b)*(s-c))
   print (v)

else:
    print"It doesn't form a triangle:"




   
