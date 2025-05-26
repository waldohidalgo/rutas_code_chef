n,k=map(int,input().split())
arr=list(map(int,input().split()))
elem=arr[0]
for i in range(1,n):
    if abs(arr[i]-k)<abs(elem-k):
        elem=arr[i]
    elif abs(arr[i]-k)==abs(elem-k):
        elem=min(arr[i],elem)
print(elem)