val=10**9+7
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr_count=[0]*(n+1)
    for elem in arr:
        if elem<=n:
            arr_count[elem]+=1
    prefixMult=[1]*(n+1)
    for i in range(1,n+1):
        prefixMult[i]=prefixMult[i-1]*arr_count[i]%val
    result=0
    for i in range(1,n+1):
        result+=prefixMult[i]%val
    print(result)