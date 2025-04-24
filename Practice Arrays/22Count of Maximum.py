t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    hs={}
    max_count=0
    elem=0
    for num in arr:
        if num in hs:
            hs[num]+=1
        else:
            hs[num]=1
        if hs[num]>max_count:
            max_count=hs[num]
            elem=num
        elif hs[num]==max_count and num<elem:
            elem=num
    print(elem,max_count)