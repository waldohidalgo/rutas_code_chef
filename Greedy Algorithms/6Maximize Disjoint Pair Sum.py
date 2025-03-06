t=int(input())
for _ in range(t):
    n,d=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    max_sum=0
    i=0
    while i<n-1:
        if arr[i]-arr[i+1]<d:
            max_sum+=arr[i+1]+arr[i]
            i+=2
        else:
            i+=1
    print(max_sum)
