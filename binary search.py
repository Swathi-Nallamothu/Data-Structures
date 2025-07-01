"""1.array must be sorted
   2.it uses divide and concer
pseudocode:
set low &high 0->n-1
condition low<=high
mid=low+high//2
a[mid]==key return mid
a[mid]<key low mid+1
a[mid]>key high mid-1
not found return -1
"""
def binary_search(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==key:
            return mid
        elif a[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
size=int(input("enetr the size of array:"))
a=[]
print("enter elements:")
for i in range(size):
    num=int(input(f"element {i+1}:"))
    a.append(num)
key=int(input("enetr the element to search:"))
result=binary_search(a,key)
if result!=-1:
    print(f"\nelement {key} found at {result}")
else:
    print(f"\nelement {key} is not found in array")
   
