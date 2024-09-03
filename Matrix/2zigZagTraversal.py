#!/c/Python312/python

# cook your dish here

n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
matrixRes=[[matrix[i][j] for j in range(m)] for i in range(n)]
isFront=True

for i in range(n):
    if isFront:
        for j in range(m):
            print(matrixRes[i][j],end=" ")
    else:
        for j in range(m-1,-1,-1):
            print(matrixRes[i][j],end=" ")
    isFront=not isFront
    