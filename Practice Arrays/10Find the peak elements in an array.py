# cook your dish here
n=int(input())
arr=list(map(int,input().split()))

prev=0
next=arr[1] if 1<n else 0
res=[]
for i in range(n):
    if arr[i]>prev and arr[i]>next:
        res.append(arr[i])
    prev=arr[i]
    next=arr[i+2] if i+2<n else 0
if res:
    print(*res)
else:
    print(-1)
