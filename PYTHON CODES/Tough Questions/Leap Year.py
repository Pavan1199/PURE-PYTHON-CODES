#Program to find whether a given year is a leap year

n=input("Enter the year:")

if n%100==0:
    if n%400==0:
        print "It is a leap year"
    else:
        print "It is not a leap year"


else:
    if n%4==0:
        print "It is a leap year"
    else:
        print "it is not a leap year"
