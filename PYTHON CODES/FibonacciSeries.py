#To print n terms of the Fibonacci Series
while 1>0:
    print"++++++++++++++++++++++++++++++++++++++++"
    print""
    n=input("Enter required number of terms : ")
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
    print""
    print""
    a=input("To terminate program press 1/ to restart press 2  :")
    if a!=2:
        print "Have a nice day! :)",exit()
