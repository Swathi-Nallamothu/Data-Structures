#we can search sorted or unsorted arrays
"""1.arr of list of size of n
   2.key for search an element
   3.start with zero index
   4.compare arr[i]==key
       arr[i]=key return index
       else not (move to next index)
   5.repeat same step till n-1
   6.if no match return -1"""
def linear_search(a,key):
    for i in range(len(a)):
        if a[i]==key:
            return i
    return -1
size=int(input("enetr the size of array:"))
a=[]
print("enter elements:")
for i in range(size):
    num=int(input(f"element {i+1}:"))
    a.append(num)
key=int(input("enetr the element to search:"))
result=linear_search(a,key)
if result!=-1:
    print(f"\nelement {key} found at {result}")
   
