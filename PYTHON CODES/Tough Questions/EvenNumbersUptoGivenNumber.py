#WAP to print all the even numbers upto a given number
n=input('Enter end point of even numbers :')
count=0
for i in range(0,n-1,2):
    i=i+2
    print i,
    count=count+i
print""
print count
