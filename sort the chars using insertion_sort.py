#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[34]:


def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
text=input("enter a string")
ch=list(text)

sort_chars=insertion_sort(ch)
print("sorted chars:",''.join(ch))



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




