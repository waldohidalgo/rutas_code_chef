# cook your dish here
n,x=map(int,input().split())
arr=list(map(int,input().split()))
for el in arr:
    if el==x:
        print("YES")
        break
else:
    print("NO")