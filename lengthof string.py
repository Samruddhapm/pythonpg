list1=input("Enter the first list of integers seperated by comma").split(',')
list2=input("Enter the first list of integers seperated by comma").split(',')
l1=len(list1)
l2=len(list2)
ln1=[]
ln2=[]
for i in list1:
    ln1.append(int(i))
for i in list2:
    ln2.append(int(i))
print("length of 1st list=",l1)
print("length of 2nd list=",l2)
if l1==l2:
    print("length of lists are same")
else:
    print("length of lists are not same")
s1=int(sum(ln1))
s2=int(sum(ln2))
print("The sum of 1st list elements are",s1)
print("The sum of 2nd list elements are",s2)
if s1==s2:
    print("The sum of list elements are same")
else:
    print("The sum of list elements are not same")
l3=[]
for i in ln1:
    if i in ln2:
        l3.append(i)
        ln2.remove(i)
print("common elemnets=",l3)