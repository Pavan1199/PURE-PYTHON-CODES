#Program to find the sum of digits
while 1>0:
    n=input("Enter number  : ")
    sum_of_digits=0
    m=n
    r=0
    while(n>0):
        digit=n%10
        sum_of_digits=sum_of_digits+digit
        r=r*10+digit
        n=n/10
    print "Sum of digits = ",sum_of_digits
    print "The reversed number = ",r
    if m==r:
        print""
        print "Yo! You just entered a palindrome! Congrats!"
        print""
    else:
        print""
        print "Loser....this isn't a palindrome.."
        print""
    a=input("Enter 1 to try again, 2 to give up on life  : ")
    if a!=1:
        print" _____________"
        print"|_____RIP_____|",exit()
