from collections import deque

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    q=deque(arr)
    count=0
    while q:
        l,r=q[0],q[-1]
        if l<r:
            count+=1
            diff=r-l
            q.popleft()
            q.pop()
            q.append(diff)
        elif l>r:
            diff=l-r
            count+=1
            q.popleft()
            q.pop()
            q.appendleft(diff)
        else:
            q.pop()
            if q:
                q.popleft()
    print(count)