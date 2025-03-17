def beautiful_pairs(arr):
    ct=0
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==(arr[j]**2):
                ct+=1
    return ct

def beautiful_pairs2(arr):
    l=max(arr)
    n=len(arr)
    hs=[0]*(l+1)
    ct=0
    for i in range(n):
        ct+=hs[arr[i]*arr[i]] if (arr[i]*arr[i])<(l+1) else 0
        hs[arr[i]]+=1
    return ct

arr=[4,4,2,2]
print(beautiful_pairs(arr))
print(beautiful_pairs2(arr))