#!/c/Python312/python

# cook your dish here
n=int(input())
arr=list(map(int,input().split()))

prefix=[0]*(n+1)
for i in range(n):
    prefix[i+1]=prefix[i]+arr[i]
    print(prefix[i+1],end=' ')