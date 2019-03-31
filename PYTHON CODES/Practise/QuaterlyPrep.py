#Preparation for the quaterly
#Fly through all the programs
#Program 1
"""PALINDROME"""
n=input("Enter a number :")
m=n
r=0
while n!=0:
    d=n%10.0
    r=r*10+d
    n=n/10
if m==r:
    print"It is a palindrome"
else:
    print"It is not a palindrome."

#Program 2
"""PRIME NUMBER CHECKER"""
print""
n=input("Enter number to be checked : ")
prime=True
if n==1:
    print "Neither prime nor composite"
else:
    for i in range(2,n):
        if (n%i==0):
            prime=False
    if (prime==True):
        print "It is a prime number."
    else:
        print"It is not a prime number."
#Program 3
"""FIBONACCI SERIES"""
print""
n=input("Enter number of terms to print :")
first=0
second=1
print first,second,
count=3
while count<=n:
    third=first+second
    print third,
    first=second
    second=third
    count=count+1
#Program 4
"""Sum of digits"""
print""
n=input("Enter number:")
sumofdigits=0
m=n
while (n>0):
    digit=n%10
    sumofdigits=sumofdigits+digit
    n=n/10
print sumofdigits

