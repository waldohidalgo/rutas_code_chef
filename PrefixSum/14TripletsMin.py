#!/c/Python312/python

# cook your dish here
t=int(input())
for testcase in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))

    arr.sort()

    counts=[]
    
    for i in range(n-2,0,-1):
        counts.append(i*(i+1)//2)
    
    lengthCounts=len(counts)
    prefixSum=[0]*(lengthCounts+1)
    
    for i in range(lengthCounts):
        prefixSum[i+1]=prefixSum[i]+counts[i]

    for query in range(q):
        k=int(input())
        left=0
        right=lengthCounts
        while left<right:
            mid=(left+right)//2
            if k>prefixSum[mid]:
                left=mid+1
            else:
                right=mid
        print(arr[left-1])
        