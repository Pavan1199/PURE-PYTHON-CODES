n=input ('enter a no')
m=2
count=0
while count < n:
    for i in range (2,m):
        if m%i==0:
            break
    else:
        print m,
        count+=1
    m+=1
