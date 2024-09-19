#!/c/Python312/python

n,k=map(int,input().split())
arr=list(map(int,input().split()))

prefix={0:1}
currentSum=0
count=0

for i in range(n):
    currentSum+=arr[i]
    if currentSum-k in prefix:
        count+=prefix[currentSum-k]
    if currentSum in prefix:
        prefix[currentSum]+=1
    else:
        prefix[currentSum]=1

print(count)