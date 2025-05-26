n=int(input())
arr=[]
for _ in range(n):
    p,q=map(int,input().split())
    arr.append((p,q))
l,r=map(int,input().split())
for p,q in arr:
    if l<=(p+q)<=r and l<=(p*q)<=r:
        print(p,q)