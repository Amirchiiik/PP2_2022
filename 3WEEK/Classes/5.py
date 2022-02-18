from os import access


class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,money):
        if money>self.balance:
            print("Error! There is no sufficient money")
        else:
            print(str(money)+"$ will be increased by 10% over 3 year period")
            print("Account balance is "+str(self.balance-trg)+"$")
    def withdraw(self,trg):
        if trg>self.balance:
            print("Error! There is no sufficient money")
        else:
            print(str(trg)+" $ was taken from your balance")
            print("Account balance is "+str(self.balance-trg)+"$")
balance=int(input("Balance:"))
name=input("Enter your name:\n")
print("Hello,"+name+",choose the following operations:")
print("Withdraw")
print("Deposit")
oper=input()
if oper=="Withdraw":
    print("Withdraw operation was selected,enter the quantity of money:")
    trg=int(input())
    a=Account(name,balance)
    a.withdraw(trg)
elif oper=='Deposit':
    print("Deposit operation was selected,choose the amount of money which will be taken:")
    trg=int(input())
    a=Account(name,balance)
    a.deposit(trg)



            