def frequency(arr):
    n=len(arr)
    res=[0]*(n+1)
    for i in range(n):
        res[arr[i]-1]+=1
    for i in range(n):
        print(res[arr[i]-1],end=" ")
    print()
        

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    frequency(arr)