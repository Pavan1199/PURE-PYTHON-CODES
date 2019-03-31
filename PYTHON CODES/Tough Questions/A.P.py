#To find the last term of an arithmetic progression

import math
a=input("Enter the starting term of AP 'a':")
n=input("Enter the number of terms of AP 'n':")
d=input("Enter the common difference of AP 'd':")

if n>=1:
    an=a+(n-1)*(d)
    print "The last term of the AP is",an

else:
    print "The information provided is invalid as the value of 'n' should always be a whole number"

