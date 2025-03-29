from collections import deque

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    q=deque(arr)
    while k:
        el=q.popleft()
        q.append(el)
        k-=1
    print(*q)