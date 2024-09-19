#!/c/Python312/python
n=int(input())
arr=list(map(int,input().split()))

countDiff={0:1}
currentSum=0
count=0

for i in range(n):
    currentSum+=arr[i]
    if currentSum-(i+1) in countDiff:
        count+=countDiff[currentSum-(i+1)]
        countDiff[currentSum-(i+1)]+=1
    else:
        countDiff[currentSum-(i+1)]=1

print(count)