#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(s,data):
        s.data=data
        s.next= None
class Linkedlist:
    def __init__(s):
        s.head=None
    def i_a_b(s,data):
        newnode=Node(data)
        newnode.next=s.head
        s.head=newnode
        print(f"{data} inserted from begin...")
    def display(s):
        current=s.head
        if not current:
            print("linked list is empty")
            return
        while current:
            print(current.data,end="---")
            current=current.next
        print(None)
        
        
l1=Linkedlist()
while True:
    print("\n Linkedlist- Insert at begin...")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice=input("enter choice")
    if choice=='1':
        data=int(input("inserted value"))
        l1.i_a_b(data)
    elif choice=="2":
        l1.display()
    elif choice=="3":
        print("exit the operation")
        break
    else:
        print("invalid choice")


# In[ ]:




