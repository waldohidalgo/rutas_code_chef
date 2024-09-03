#!/c/Python312/python

# cook your dish here
n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]


def dfs(i,j):
    if i<0 or j<0 or i>=n or j>=m or matrix[i][j]==0:
        return 0
    matrix[i][j]=0
    return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

maxArea=0
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            maxArea=max(maxArea,dfs(i,j))
print(maxArea)