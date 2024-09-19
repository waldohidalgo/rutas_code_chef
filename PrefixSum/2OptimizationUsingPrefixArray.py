#!/c/Python312/python

# cook your dish here
n=int(input())
arr=list(map(int,input().split()))
k=int(input())


prefixSum=[0]*(n+1)
# complexity of prefix sum is O(n)
for i in range(n):
    prefixSum[i+1]=prefixSum[i]+arr[i]

# complexity of queries is O(k)
for query in range(k):
    i,j=map(int,input().split())
    print(prefixSum[j]-prefixSum[i-1])