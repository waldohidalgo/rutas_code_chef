#!/c/Python312/python
# cook your dish here
t=int(input())

arrs=[]
for _ in range(t):
    n=int(input())
    arrs.append(list(map(int,input().split())))

def calculateMinSumIndex(arr):
    n=len(arr)
    if n==0:
        return -1
    
    prefixSum=arr[0]
    suffixSum=sum(arr)
    minSum=prefixSum+suffixSum
    indexMin=0

    for i in range(1,n):
        prefixSum+=arr[i]
        suffixSum-=arr[i-1]
        if prefixSum+suffixSum<minSum:
            minSum=prefixSum+suffixSum
            indexMin=i

    return indexMin+1

for arr in arrs:
    print(calculateMinSumIndex(arr))

