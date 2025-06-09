# cook your dish here
n,m=map(int,input().split())
best_friends=set(map(int,input().split()))


friends=[]
other=[]
for _ in range(m):
    read=input().split()
    f=int(read[0])
    p=int(read[1])
    s=read[2]
    if f in best_friends:
        friends.append((-p,s))
    else:
        other.append((-p,s))

friends.sort()
other.sort()

for p in friends:
    print(p[1])
for p in other:
    print(p[1])