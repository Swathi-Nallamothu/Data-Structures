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
    def iae(s,data):
        newnode=Node(data)
        if s.head is None:
            s.head=newnode
            return
        temp= s.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def backtraverse(s):
        print("values for traversing backward...")
        temp=s.head
        if not temp:
            print("empty list")
            return 
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end="<--->")
            temp=temp.prev
        print("None")
    def display(s):
        temp=s.head
        print("Double Linked List:")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DLL()
n=int(input("enter the no of elements to insert at end"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iae(val)
dll.display()
dll.backtraverse()


# In[ ]:




