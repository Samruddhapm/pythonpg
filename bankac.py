class bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amt):
        if amt<=0:
            print("It should be an positive number")
        else:
            self.bal+amt
            print("Your current balance is",self.bal)
    def withdraw(self,amt):
        if amt<= 0:
            print("It should be an positive number")
        elif amt>self.bal:
            print("Insufficient balance")
        else:
            self.bal-=amt
            print("Your current balance is", self.bal)
    def display(self):
        print(f" Account number:{self.accno}")
        print(f" Account holder:{self.name}")
        print(f" Account type:{self.type}")
        print(f" Account balance:{self.bal}")
no=int(input("Enter the account number"))
name=input("Enter your name")
type=input("Enter the account type")
bal=int(input("Enter your current account balance"))
usr1=bank(no,name,type,bal)
while True:
    print("\n1)DEPOSIT\n2)WITHDRAWAL\n3)ACCOUNT INFORMATION\n4)EXIT\n")
    opt=int(input("enter the option"))
    if opt==1:
        amt=int(input("enter your amount"))
        usr1.deposit(amt)
    elif opt==2:
        amt=int(input("enter your withdrawal amount"))
        usr1.withdraw(amt)
    elif opt==3:
         usr1.display()
    elif opt==4:
        exit(0)
    else:
        print("invalid option")


