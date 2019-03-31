n=input("Enter the number:")
s=0
m=n
while(n>0):
       p = n%10
       s=s +(p**3)
       n=n/10
if s==m:
       print "It is an armstrong number"
else:
       print "It is not an armstrong number"
        
      
    
