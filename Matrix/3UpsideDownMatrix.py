#!/c/Python312/python

# cook your dish here

n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
matrixRes=[[matrix[i][j] for j in range(m)] for i in range(n)]

for i in range(n-1,-1,-1):
    for j in range(m):
        print(matrixRes[i][j],end=" ")
    print()