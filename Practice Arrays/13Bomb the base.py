t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        if arr[i]<x:
            print(i+1)
            break
    print(0)