#!/c/Python312/python

mod = 10**9 + 7

t = int(input())

arrResult=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Write your solution here
    res=1
    for elem in a:
        res*=(elem+1)
    arrResult.append(res%mod)

for elem in arrResult:
    print(elem)
    