#Finding the nature of the roots and the roots of a quadratic equation

import math
a=input ("Enter the coefficient of x2:")
b=input ("Enter the coefficient of x:")
c=input ("Enter the coefficient of constant:")

D = b**2 - 4*a*c

if D > 0:
   print "Real and unequal roots"
   if D>0:

        x = (-1*b + D**0.5) / (2*a)
        y = (-1*b - D**0.5) / (2*a)

   elif D == 0:
        x = (-1*b + D**0.5) / (2*a)
        y = (-1*b - D**0.5) / (2*a)

   print "The roots of the quadratic equation are:",x,y
elif D == 0:
   print "Real and equal roots"
   if D>0:

        x = (-1*b + D**0.5) / (2*a)
        y = (-1*b - D**0.5) / (2*a)

   elif D == 0:
        x = (-1*b + D**0.5) / (2*a)
        y = (-1*b - D**0.5) / (2*a)

   print "The roots of the quadratic equation are:",x,y
else:
   print "Real roots do not exist"





