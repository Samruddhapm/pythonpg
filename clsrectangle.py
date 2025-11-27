class rectangle:
    def __init__(self,l,w):
        self.__length=1
        self.__width=w
    def area(self):
        return self.__length*self.__width
    def __lt__(self,other):
        if self.area()<other.area():
            return True
        else:
            return False
l1=int(input("Enter the length:"))
w1=int(input("Enter the width:"))
r1=rectangle(l1,w1)
l2 = int(input("Enter the length of second rectangle:"))
w2 = int(input("Enter the width of second rectangle:"))
r2=rectangle(l2,w2)
if r1<r2:
    print(f"Area of r2 is greater:{r2.area()}")
else:
    print(f"Area of r1 is greater:{r1.area()}")




