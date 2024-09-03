#!/c/Python312/python

# cook your dish here

n,m=map(int,input().split())

matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

zerosIndex=[]
for i in range(n):
    for j in range(m):
        if matrix[i][j]==0:
            zerosIndex.append([i,j])

for k in range(len(zerosIndex)):
    i,j=zerosIndex[k]
    for k in range(m):
        if matrix[i][k]!=0:
            matrix[i][k]=0    
    for k in range(n):
        if matrix[k][j]!=0:
            matrix[k][j]=0

for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()