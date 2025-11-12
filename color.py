n = int(input("Enter the limit of clr: "))
li=[]

for i in range(n):
    element = input(f"Enter color {i+1}: ")
    li.append(element)

print("List:",li)
print("first color=",li[0])
print("last color=",li[-1])
