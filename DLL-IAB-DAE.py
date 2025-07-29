#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
    def dae(s):
        if s.head is None:
            print("cats perform delete in empty list...")
            return
        temp=s.head
        while temp.next:
            temp=temp.next
        print(f"deleted:{temp.data}")
        if temp.prev:
            temp.prev.next=None
        else:
            s.head=None
            
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
d=int(input("\n enter ow many times you want to perform delete operation"))
for _ in range(d):
    dll.dae()
    dll.display()


# In[ ]:




