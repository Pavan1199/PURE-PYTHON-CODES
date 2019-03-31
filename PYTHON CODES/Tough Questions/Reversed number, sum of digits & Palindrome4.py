n=input("Enter a multidigit number:")
m=n
sum=0
while(n>0):
       p = n%10
       sum = sum+p
       n = n//10

print "Sum of digits of ",m," is ",sum;

n=m
reverse=0

while(n>0):
       digit=n%10
       reverse=reverse*10+digit
       n=n/10

print "The Reversed Number  ",reverse
if (m==reverse):
       print "It is Palindrome"
else:
     print "It is not Palindrome"

print sum(1,5[0])
print __getitem__
