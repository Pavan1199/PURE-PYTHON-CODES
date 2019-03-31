#WAP to print the exponent if a number(without using import.math or **)
base=input('Enter base no.')
ex=input('Enter exponent')
p=1
for i in range (1,ex+1,1):
    p=p*base
print base,'raised to ',ex,'=',p
