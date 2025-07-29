#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(s, data):
        s.data = data
        s.prev = None
        s.next = None

class DLL:
    def __init__(s):
        s.head = None

    def iab(s, data):
        newnode = Node(data)
        newnode.next = s.head
        if s.head:
            s.head.prev = newnode
        s.head = newnode
    def display(s):
        temp = s.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def count_duplicates(s):
        temp = s.head
        freq = {}
        while temp:
            freq[temp.data] = freq.get(temp.data, 0) + 1
            temp = temp.next

        print("\nDuplicate Counts:")
        for key, count in freq.items():
            print(f"{key} occurs {count} times")
dll=DLL()
n=int(input("enter the no of elements to insert at begin"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iab(val)
dll.display()
dll.count_duplicates()


# In[ ]:




