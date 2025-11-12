word=input("Enter the word seperate by space").split()
name=0
for i in word:
    name+=i.lower().count('a')
print(name)


