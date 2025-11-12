list=input("Enter the list of integers:").split()
rlist=[]
for i in list:
    num=int(i)
    if num>100:
        rlist.append("over")
    else:
        rlist.append(num)
print(rlist)