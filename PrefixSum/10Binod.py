#!/c/Python312/python

# cook your dish here
T=int(input())

for t in range(T):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    prefixSetUnset=[{"set":[0]*(n+1),"unset":[0]*(n+1)} for _ in range(60)]
    for k in range(60):
        for i in range(n):
            if arr[i]&(1<<k):
                prefixSetUnset[k]["set"][i+1]=prefixSetUnset[k]["set"][i]+1
                prefixSetUnset[k]["unset"][i+1]=prefixSetUnset[k]["unset"][i]
            else:
                prefixSetUnset[k]["set"][i+1]=prefixSetUnset[k]["set"][i]
                prefixSetUnset[k]["unset"][i+1]=prefixSetUnset[k]["unset"][i]+1
    
    for query in range(q):
        k,l1,r1,l2,r2=map(int,input().split())
        countSetBitBetweenL1R1=prefixSetUnset[k]["set"][r1]-prefixSetUnset[k]["set"][l1-1]
        countSetBitBetweenL2R2=prefixSetUnset[k]["set"][r2]-prefixSetUnset[k]["set"][l2-1]
        countUnsetBitBetweenL1R1=prefixSetUnset[k]["unset"][r1]-prefixSetUnset[k]["unset"][l1-1]
        countUnsetBitBetweenL2R2=prefixSetUnset[k]["unset"][r2]-prefixSetUnset[k]["unset"][l2-1]
        print(countSetBitBetweenL1R1*countUnsetBitBetweenL2R2+countSetBitBetweenL2R2*countUnsetBitBetweenL1R1)
        
