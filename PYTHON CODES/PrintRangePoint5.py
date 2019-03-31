#Program print the numbers between the given range and find their sum
a=input("Enter final number : ")
count=0
sum_=0
for i in range(0,a,1):
    i=i+0.5
    print i,
    count = count+1
    sum_=sum_+i
print "The count is : ",count
print "The sum is : ", sum_
