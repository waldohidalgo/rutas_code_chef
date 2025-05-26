
arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]

print(*arr)