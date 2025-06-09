# cook your dish here
import heapq

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    total=sum(arr)
    heapq.heapify(arr)
    son=[]
    for i in range(min(k,n-k)):
        son.append(heapq.heappop(arr))
    group1=sum(son)
    group2=total-group1
    print(abs(group2-group1))