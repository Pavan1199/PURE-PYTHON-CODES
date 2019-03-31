n=input("Enter a number : ")
m=n
r=0
while n!=0:
    d=n%10.0
    r=r*10+d
    n=n/10
if m==r:
    print "It's a palindrome."
else:
    print"It's not a palindrome."
