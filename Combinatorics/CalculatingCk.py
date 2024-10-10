mod = 10**9 + 7
N = 2001
C = [[-1] * N for _ in range(N)]

def combinations(n, k):
    if n == k or k == 0:
        return 1
    if k > n:
        return 0
    if C[n][k] != -1:
        return C[n][k]

    C[n][k] = (combinations(n - 1, k - 1) + combinations(n - 1, k)) % mod

    return C[n][k]

if __name__ == "__main__":
    for i in range(N):
        for j in range(N):
            C[i][j] = -1
        
    n = 7
    k = 3
    print(f"{n}C{k} is: {combinations(n, k)}")
