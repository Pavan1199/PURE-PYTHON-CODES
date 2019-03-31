# Program to find prime numbers between two given numbers

a=input("Enter the value of the first number:")
b=input("Enter the value of the second number:")
print "the prime no.s from ",a, "to",b, "are:-"
for i in range(a,b+1,1):
    prime=True
    for f in range(2,i):
        if i%f==0:
            prime=False
        else:
            pass
    if prime==True:
        print i,
    else:
        pass
        
