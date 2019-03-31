#WAP TO INPUT THREE NUMBERS AND CHECK WHETHER THEY FORM A TRIANGLE
a=input("Enter first side  : ")
b=input("Enter second side  : ")
c=input("Enter third side : ")
if a<b+c and b<a+c and c<a+b:
    print "It's a triangle!"
    if a==b==c:
        print "It's an equilateral triangle.."
    elif a==b or b==c or a==c:
        print "It is an isoceles triangle.."
    else:
        print" It's a scalene triangle.."
    if a**2==b**2+c**2 or b**2==c**2+a**2 or c**2==a**2+b**2:
        print "It's a right angle triangle.."
    else:
        print"It's not a right angled triangle.."
    s=(a+b+c)/2.0
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print "Semi-perimeter  = ",s
    print "Area  = ",area
else:
    print"It is not a triangle "
