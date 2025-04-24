# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        if arr[i]>k:
            count+=1
    print(count)