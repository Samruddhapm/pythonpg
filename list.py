r=int(input("Enter the range of list"))
numb=[]
for i in range(r):
    num1 = int(input(f"Enter the list elements {i+1}"))
    numb.append(num1)
print("Inserted list")
print(numb)
num2=[]
for num in numb:
    if num>0:
        num2.append(num)
print("positive list")
print(num2)