#!/usr/bin/env python
# coding: utf-8

# In[20]:


def count_sort(a,exp):
    n=len(a)
    output=[0]*n
    count=[0]*10#for empty bucket
    for i in range(n):
        index= (a[i]//exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=(a[i]//exp)%10
        output[count[index]-1]=a[i]
        count[index]-=1
        i-=1
    for i in range(n):
        a[i]=output[i]
def radix_sort(a):
    max_num=max(a)
    exp=1
    while max_num//exp >0:
        count_sort(a,exp)
        exp*=10
        
a=[170,45,75,90,802,24,2,66]
print("before sort:",a)
radix_sort(a)
print("after sort:",a)


# In[ ]:





# In[ ]:




