#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Transaction:
    def __init__(s,operation,amount):
        s.type=operation
        s.amount=amount
        s.next= None
class TransactionHistory:
    def __init__(s):
        s.head=None
    def add_transaction(s,operation,amount):
        no_trans=Transaction(operation,amount)
        if not s.head:
            s.head=no_trans
        else:
            current=s.head
            while current.next:
                current=current.next
            current.next=no_trans
        print(f"{operation} of Rs{amount} recorded")
    def show_history(s):
        if not s.head:
            print("no transaction found")
            return
        print("\n transaction history")
        current=s.head
        count=1
        while current:
            print(f"{count}.{current.type}-Rs{current.amount}")
            current=current.next
            count+=1
        
history=TransactionHistory()
while True:
    print("\n-------ATM Transaction Menu-----")
    print("1.Deposit")
    print("2. Withdraw")
    print("3.history")
    print("4.exit")
    choice=input("enter your choice")
    if choice=="1":
        amount=float(input("enter amount to deposit:"))
        history.add_transaction("deposit",amount)
    elif choice=="2":
        amount=float(input("enter amount to withdraw"))
        history.add_transaction("withdraw",amount)
    elif choice=="3":
        history.show_history()
    elif choice=="4":
        print("end of transaction....exit")
        break
    else:
        print("choose 1/2/3/4 only......")

