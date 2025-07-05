#!/usr/bin/env python
# coding: utf-8

# In[2]:


def selection_sort(a1):
    n=len(a1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if a1[j]<a1[min_index]:
                min_index=j
                a1[i],a1[min_index]=a1[min_index],a1[i]
    return a1
size=int(input("enter the no of elements:"))
a1=[]
print("eneter",size,"elements")
for _ in range(size):
    num=int(input())
    a1.append(num)
result=selection_sort(a1)
print("sorted array",result)


# In[ ]:




