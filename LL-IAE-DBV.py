#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(s,data):
        s.data=data
        s.next= None
class Linkedlist:
    def __init__(s):
        s.head=None
    def i_a_E(s,data):
        newnode=Node(data)
        if s.head is None:
            s.head=newnode
            print(f"{data} inserted at end / will be first node")
            return
        current=s.head
        while current.next:
            current=current.next
        current.next=newnode
        print(f"{data} inserted at last")
    def delete_by_value(s, value):
        current = s.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    s.head = current.next
                print(f"Deleted node with value: {value}")
                return
            prev = current
            current = current.next
        print(f"Value {value} not found in linked list")
    
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
    print("3. delete")
    print("4. Exit")
    
    choice=input("enter choice")
    if choice=='1':
        data=int(input("inserted value"))
        l1.i_a_E(data)
    elif choice=="2":
        l1.display()
    elif choice=="3":
        v=int(input("value"))
        l1.delete_by_value(v)
    elif choice=="4":
        print("exit the operation")
        break
    else:
        print("invalid choice")


# In[ ]:




