#Program to find the whether a given number is prime or composite
n=input("Enter a number:")

F=1
for i in range(1,n,1):
    F=F*i

if  (F+1)%n==0:
    print "It is a prime number"
elif n==1:
    print "1 is neither composite nor prime. Enter another value"
else:
    print "It is a composite number:"





