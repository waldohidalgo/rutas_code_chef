n,k=map(int,input().split())

for _ in range(n):
    p,q=map(int,input().split())
    if (p+q)%k==0:
        print("({a},{b})".format(a=p,b=q))