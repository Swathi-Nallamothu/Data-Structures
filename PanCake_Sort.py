#!/usr/bin/env python
# coding: utf-8

# In[26]:


"""algorithm:
   1. start complete array and decrease the size(n-)
   2. for each size:
     a). find the index o max element
     b). flip the array with max element index
     c). flip the total array to the current size
     max->move to the end of the array
   3. repeat s1 by n-2,n-3........
   for nth reduced element perform s2 untill oth index value respectively
   """
def flip(a,k):
    return a[:k+1][::-1]+a[k+1:]
def pancake(a):
    n=len(a)
    for size in range(n,1,-1):
        max_index=a.index(max(a[:size]))
        if max_index!=size-1:
            if max_index!=0:
                a=flip(a,max_index)
                print(f" flip at {max_index+1}:{a}")
            a=flip(a,size-1)
            print(f" flip at {size}:{a}")
    return a
nums=list(map(int,input("enter n separated with space:").split()))
sorted_nums=pancake(nums)
print("sorted numbers",sorted_nums)


# In[ ]:





# In[ ]:




