while (1>0):
    print"__Welcome to Python Calculator 1.0__"
    a=input("Enter First Number:  ")
    b=input("Enter Second Number:  ")
    print""
    c=raw_input("Choose your operator( + or - or * or /) : ")
    if c==("+"):
        print"          The solution is:  ",a+b
    elif c==("-"):
        print"          The difference is:  ",a-b
    elif c==("*"):
        print"          The product is:  ",a*b
    elif c==("/"):
        d=float(a)/float(b)
        print"          The quotient is:  ",("%.2f"%d)
    else:
        print" :x__WRONG INPUT__x: ",exit()
    print
    print"Thank You For Using Python Calculator 1.0"
    end=input("To exit press 1/To restart calculator press 2 :  ")
    if end!=2:
        print"GoodBye! :)",exit()
