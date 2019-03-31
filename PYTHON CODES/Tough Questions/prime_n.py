#program to print the prime no's upto n
a=input('enter no of prime nos:')
s=0
n=2
while s<a:
    prime=True
    for i in range (2,n):
        if (n % i==0):
            prime=False
    if prime==True:
        print n,
        s=s+1
    n=n+1
            
            
