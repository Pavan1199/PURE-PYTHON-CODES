n=input("Enter the number of names:")
a=0
for i in range(1,n+1):
    b=raw_input("Enter the name:")
    if b>a:
        a=b
print a
