n=int(input())
arr=list(map(int,input().split()))
stack=[]
res=[-1]*n
for i in range(n-1,-1,-1):
    while stack and stack[-1]<=arr[i]:
        stack.pop()
    if stack:
        res[i]=stack[-1]
    stack.append(arr[i])

print(*res)