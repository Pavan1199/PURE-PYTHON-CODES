'''program to input a multidigit no. and
1)print sum
2)print the reverse number
3)check whether the given no. is a palindrome '''
n=input("Enter A Multidigit Number:")
i=1
s=0
while n>i:
    f=i*10
    x=(n%f)
    x=x/i
    s=s+x
    i*=10
print 'Sum Of The Digits Is', s
m=n
r=0
while n!=0:
    d=n%10
    r=r*10+d
    n=n/10
print'The Reverse of the no. is', r
if m==r:
    print'It is a palindrome'
else:
    print'It is not a palindrome'
