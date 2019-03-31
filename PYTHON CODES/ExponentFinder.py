#Program to calculate the exponentials.
base=input("Enter the base value : ")
ex=input("Enter exponent : ")
p=1
for i in range(1,ex+1,1):
    p=p*base
print base,"raised to exponent",ex," = ",p
