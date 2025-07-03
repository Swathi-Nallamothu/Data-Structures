def bsearch_range(a1,target,left,right):
    while left<=right:
        mid=(left+right)//2
        if a1[mid]==target:
            return mid
        elif a1[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
def expo_search(a1,target):
    if not a1:
        return -1
    elif a1[0]==target:
        return 0
    n=len(a1)
    i=1
    while i<n and a1[i]<=target:
        i*=2
    return bsearch_range(a1,target,i//2,min(i,n-1))
a1=[2,4,6,8,10,12,14]
target=10
result=expo_search(a1,target)
print(f"Element {target} found at index:{result}")
