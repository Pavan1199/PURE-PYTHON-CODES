import random, math

class Bank:
  
    def __init__(self):
        self.__acc_no=" "
        self.__balance=1000.0
        self.__name=" "

    def storedata(self):
      
        r=[]
        self.__name=raw_input("\nEnter the name of account-holder - ")
        self.__acc_no=str(random.random())[2:6]
        while self.__acc_no in r:
            self.__acc_no=str(random.random())[2:6]
        r.append(self.__acc_no)

    def displaydata(self):
      
        print "\n\n"
        print "Account number:",self.__acc_no
        print "Name of Account-holder:",self.__name
        print "Balance:",self.__balance,"AED"

    def deposit(self):
      
        amt=math.fabs(float(input("\nEnter the amount to be deposited - ")))
        self.__balance+=amt
        print "\nAmount successfully deposited!"
        self.displaydata()

    def withdraw(self):
      
        amt=math.fabs(float(input("\nEnter the amount to withdraw - ")))
        if self.__balance-amt>=1000:
            print "\nAmount Successfully withdrawn!"
            self.__balance-=amt
            self.displaydata()
        else:
            print "\nMinimum balance should be 1000 AED"

    def check(self):
        
        if self.__balance>=5000:
            self.displaydata()   

    def give(self):
        return self.__acc_no

n=input("\nEnter the number of accounts - ")

accounts=range(n)

for i in range(n):
    accounts[i]=Bank()
    accounts[i].storedata()
    accounts[i].displaydata()
    
while True:
  
    print "\n\t\tMENU"
    print "\t1 --> Customer"
    print "\t2 --> Manager"
    print "\t3 --> Exit"
    
    choice=input("\nEnter your choice - ")
    
    if choice==1:
        a_n=raw_input("\nEnter your account number - ")
        for i in range(n):
            a=accounts[i].give()
            if a_n==a:
                ind=i
                break
        else:
            print "\nIncorrect account number!"

        while True:
          
            print "\n\t\tMENU"
            print "\t1 --> Display Account Info"
            print "\t2 --> Deposit"
            print "\t3 --> Withdraw"
            print "\t4 --> Exit"

            choice=input("\nEnter your choice - ")

            if choice==1:
                accounts[ind].displaydata()
            elif choice==2:
                accounts[ind].deposit()
            elif choice==3:
                accounts[ind].withdraw()
            elif choice==4:
                print "\nExiting..."
                break
              
    elif choice==2:
      
        while True:
          
            print "\n\t\tMENU"
            print "\t1 --> Check for Outstanding Account holders"
            print "\t2 --> Check Account"
            print "\t3 --> Exit"

            choice=input("\nEnter your choice - ")
            
            if choice==1:
                print "\nAccounts whose balance is equal to or exceeds 5000 AED"
                for i in range(n):
                    accounts[i].check()
            elif choice==2:
                a_n=raw_input("\nEnter the account number to check - ")
                for i in range(n):
                    a=accounts[i].give()
                    if a==a_n:
                        accounts[i].displaydata()
                        break
                else:
                    print "\nAccount not found!"
            elif choice==3:
                print "\nExiting..."
                break
            else:
                print "\nIncorrect choice! Try again!"
                
    elif choice==3:
        print "\nExiting..."
        exit()
    else:
        print "\nIncorrect choice! Try again!"

class Library:
  
    def __init__(self):
      
        self.b_no=0
        self.b_name=""
        self.author=""
        self.pub=""
        self.price=0.0
        self.no_of_copies=0
        self.no_of_copies_iss=0

    def storedata(self):
      
        self.b_no=raw_input("\nEnter the book number - ")

        if self.b_no in nos:
            print "\nBOOK NUMBER ALREADY EXISTS! TRY AGAIN!"
            self.storedata()
            
        self.b_name=raw_input("Enter the book name - ")
        self.author=raw_input("Enter name of author - ")
        self.pub=raw_input("Enter name of publisher - ")
        self.price=float(input("Enter the book price - "))
        self.no_of_copies=input("Enter the number of copies - ")

    def issue(self):
        if self.no_of_copies==self.no_of_copies_is:
                  print "\n\nSorry! Book currently unavailable!".upper()
        else:
            self.no_of_copies_iss+=1
            self.no_of_copies-=1
            print "\n\n\t\tBook issued!".upper()
            self.display()            

    def return_book(self):
      
        if self.no_of_copies_iss>0:
            print "\nBook returned!"
            print "\nThank you! Visit us again!"
            self.no_of_copies_iss-=1
            self.no_of_copies+=1
        else:
            print "\nBook not issued!"

    def display(self):
        
        print "\nBook number:",self.b_no
        print "Book name:",self.b_name
        print "Author:",self.author
        print "Publisher:",self.pub
        print "Price:",self.price
        print "Available copies:",self.no_of_copies-self.no_of_copies_iss

n=input("\nEnter the number of books in the library - ")
s=range(n)
nos=[]

for i in range(n):
  
    print "\nBook",i+1,":"
    s[i]=Library()
    s[i].storedata()
    nos.append(s[i].b_no)

while True:
  
    print "\n\t\t\tMENU"
    print "\n\t1 --> Display Book Information"
    print "\t2 --> Issue a Book"
    print "\t3 --> Return a Book"
    print "\t4 --> Exit"

    choice=input("\nEnter your choice - ")

    if choice==1:
        bno=raw_input("\nEnter the book number - ")
        for i in range(n):
            if s[i].b_no==bno:
                s[i].display()
    elif choice==2:
        bno=raw_input("\nEnter the book number - ")
        for i in range(n):
            if s[i].b_no==bno:
                s[i].issue()
    elif choice==3:
        bno=raw_input("\nEnter the book number - ")
        for i in range(n):
            if s[i].b_no==bno:
                s[i].return_book()
    elif choice==4:
        print "\nExiting..."
        exit()        
