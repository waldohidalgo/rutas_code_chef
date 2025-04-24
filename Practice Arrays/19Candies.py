t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count={}
    isPossible=True
    for num in arr:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
        if count[num]>2:
            isPossible=False
            break

    print("Yes" if isPossible else "No")