#To identify the integer
num=input("Enter number: ")
if num<0:
    print "It is negative"
elif num>0:
    print"It is positive"
elif num==0:
    print"It is zero"
else:
    print"MIND----->BOOM!",exit()
#To check if it's a prime number
prime=True
if num==1:
    print "It is neither prime nor composite"
else:
    for i in range(2,num):
        if (num%i==0):
            print "It's a prime number."            
        else:
            print "It's not a prime number.",exit()
#To Check if it's a palindrome
n=num
r=0
while n!=0:
    d=n%10.0
    r=r*10+d
    n=n/10
if n==r:
    print "It's a palindrome."
else:
    print"It's not a palindrome."
#To check whether it is divisible by 3
if num%3==0:
    print "It is divisible by 3"
else:
    print "It is not divisble by 3"
#To check if the given number is an armstrong number
sum=0
temp=num
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10
if arm==sum:
    print num,"is an armstrong number"
else:
    print num, "is not an armstrong number"
