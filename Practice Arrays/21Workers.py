n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

min_t=pow(10,5)+1
min_a=pow(10,5)+1
min_m=pow(10,5)+1


for i in range(n):
    if t[i]==1:
        min_t=min(min_t,c[i])
    elif t[i]==2:
        min_a=min(min_a,c[i])
    else:
        min_m=min(min_m,c[i])

if min_t+min_a<min_m:
    print(min_t+min_a)
else:
    print(min_m)