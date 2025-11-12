n=int(input("Enter the limit of series"))
n1=0
n2=1
print(n1)
print(n2)
while n>=3:
     n3=n1+n2
     print(n3)
     n1=n2
     n2=n3
     n=n-1