n= int(input("Enter the limit of the list: "))
li=[]
for i in range(n):
    element = int(input(f"Enter the list elements {i+1}: "))
    li.append(element)
s=sum(li)
print("sum=",s)