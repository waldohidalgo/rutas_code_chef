#!/c/Python312/python

# cook your dish here
n,m=map(int,input().split())
matrix1=[]
for i in range(n):
    matrix1.append(list(map(int,input().split())))
matrix2=[]
for i in range(n):
    matrix2.append(list(map(int,input().split())))
matrixRes=[[matrix1[i][j]+matrix2[i][j] for j in range(m)] for i in range(n) ]


for i in range(n):
    for j in range(m):
        print(matrixRes[i][j],end=" ")
    print()