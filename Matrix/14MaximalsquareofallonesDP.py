n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


memo = [[0] * n for _ in range(n)]
maxSquareSize = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            if i == 0 or j == 0:
                memo[i][j] = 1 
            else:
                memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
            maxSquareSize = max(maxSquareSize, memo[i][j])

print(maxSquareSize ** 2)
