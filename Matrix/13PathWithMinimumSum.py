#!/c/Python312/python

# cook your dish here

n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))


memo=[[0 for j in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            memo[i][j]=matrix[i][j]
        elif i==0:
            memo[i][j]=memo[i][j-1]+matrix[i][j]
        elif j==0:
            memo[i][j]=memo[i-1][j]+matrix[i][j]
        else:
            memo[i][j]=min(memo[i-1][j],memo[i][j-1])+matrix[i][j]

print(memo[n-1][m-1])        
