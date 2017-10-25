import math
n=int(input("enter the choice"))
a=int(input("enter 1st number"))
b=int(input("enter second number"))
if n==1:
    print('sum is',a+b)
elif n==2:
    print('sub is',a-b)
elif n==3:
    print(a*b)
else:
    print('invalid')
