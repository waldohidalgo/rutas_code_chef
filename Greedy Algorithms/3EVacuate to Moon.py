t=int(input())
for _ in range(t):
    n,m,h=list(map(int,input().split()))
    arr_n=list(map(int,input().split()))
    arr_m=list(map(int,input().split()))
    arr_n.sort(reverse=True)
    arr_m.sort(reverse=True)
    ct=0
    for i in range(min(n,m)):
        ct+=min(arr_n[i],arr_m[i]*h)
    print("res",ct)