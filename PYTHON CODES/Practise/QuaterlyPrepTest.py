#palindrome
n=input("Enter number:")
m=n
r=0
while n!=0:
    digit=n%10
    r=r*10+digit
    n=n/10
if m==r:
    print"yes"
else:
    print"no"
#Primenumber checker
print""
n=input("Enter prime number")
prime=True
if n==1:
    print"Neither prime nor composite"
else :
    for i in range(2,n):
        n%2==0
        prime=False
    if prime==False:
        print"Not prime"
    else:
        print"Prime"

#fibonacci
n=input("Enter numbr of terms")
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

#sumofdigits
print""
n=input("Enter number:")
sod=0
m=n
while(n>0):
    d=n%10
    sod=sod+d
    n=n/10
print sod
