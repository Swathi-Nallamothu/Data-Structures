import math
def jump_search(a1,target):
    if not a1:
        return -1
    n=len(a1)
    step=int(math.sqrt(n))
    prev=0
    while prev<n and a1[prev]<target:
        prev+=step
    for i in range(max(0,prev-step),min(n,prev+1)):
        if a1[i]==target:
            return i
    return -1
        
a1=[1,3,5,7,8,9,11]
target=7
result=jump_search(a1,target)
print(f"element {target} found at index:{result}")
