from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

mp = defaultdict(int)
ct=0
for i in range(n):
    ct+=mp[a[i]*a[i]]
    mp[a[i]]+=1
print(ct)
