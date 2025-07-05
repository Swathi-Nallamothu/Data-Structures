#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and len(a[j])>len(key):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
n=int(input("no.of elements"))
a=[]
print("enter",n,"elements")
for _ in range(n):
    num=input()
    
    a.append(num)
result=insertion_sort(a)
print("sorted array:",result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




