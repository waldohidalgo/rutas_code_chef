n=int(input())
arr=list(map(int,input().split()))
k=int(input())
res=[0]*k
for i in range(n):
    res[arr[i]]+=1
prev=0
for j in range(k):
    res[j]+=prev
    prev=res[j]

print(*res)