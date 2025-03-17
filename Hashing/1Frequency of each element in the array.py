def frequency(arr):
    n=len(arr)
    for i in range(n):
        ct=0
        for j in range(n):
            if arr[i]==arr[j]:
                ct+=1
        print(ct,end=" ")
    print()
        

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    frequency(arr)