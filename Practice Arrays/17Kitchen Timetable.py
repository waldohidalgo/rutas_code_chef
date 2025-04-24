t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    students=list(map(int,input().split()))
    count=0
    start=0
    for i in range(n):
        end=arr[i]
        dist=end-start
        if students[i]<=dist:
            count+=1
        start=end
    print(count)


