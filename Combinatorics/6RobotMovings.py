mod = 10**9 + 7
N = 5001


combinations = [[0]*N for _ in range(N)]

def dp_combinations():
    for n in range(N):
        combinations[n][0] = 1 
        for k in range(1, n + 1):
            combinations[n][k] = (combinations[n - 1][k - 1] + combinations[n - 1][k]) % mod


dp_combinations()  

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    if k>=2*(n-1):
        print(0)
        continue
    bar=k//2
    if k%2==0:
        result = (combinations[n - 2][bar] * 2 * combinations[n - 2][bar-1]) % mod
    else:
        result = (combinations[n - 2][bar] * 2 * combinations[n - 2][bar]) % mod
    print(result)


