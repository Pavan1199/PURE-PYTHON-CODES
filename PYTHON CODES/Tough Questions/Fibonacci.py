#program to print the fibonaccci series
n=input('Enter no of digits :-')
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
    
