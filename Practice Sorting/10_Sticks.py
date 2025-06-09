t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    s1=None
    s2=None
    i=0
    while i<n:
        if s1 is None and i+1<n and arr[i]==arr[i+1]:
            s1=arr[i]
            i+=2
        if s1:
            if i+1<n and arr[i]==arr[i+1]:
                s2=arr[i]
                break
        i+=1

    if s1 and s2:
        print(s1*s2)
    else:
        print(-1)
    print(arr)
    print("s1",s1)
    print("s2",s2)


            