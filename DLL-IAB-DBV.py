#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(s,data):
        s.data=data
        s.prev=None
        s.next=None
class DLL:
    def __init__(s):
        s.head=None
    def iab(s,data):
        newnode=Node(data)
        newnode.next=s.head
        if s.head:
            s.head.prev=newnode
        s.head=newnode
        temp= s.head
    def  dbv(s,value):
        temp=s.head
        while temp:
            if temp.data==value:
                print(f"Deleted:{temp.data}")
                if temp.prev:
                    temp.prev.next=temp.next
                else:
                    s.head=temp.next
                if temp.next:
                    temp.next.prev=temp.prev
                return
            temp=temp.next
        print(f"{value} not found in the list")
       
           
           
    def display(s):
        temp=s.head
        print("Double Linked List:")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DLL()
n=int(input("enter the no of elements to insert at begin"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iab(val)
dll.display()
d=int(input("\n how many times you want to perform delete op:"))
for i in range(d):
   
    val=int(input("enter value to delete"))
    dll.dbv(val)
    dll.display()


# In[ ]:




