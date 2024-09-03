#!/c/Python312/python

# cook your dish here
from collections import deque

n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]

aux=[[float('inf')]*m for _ in range(n)]

queue=deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j]==0:
            aux[i][j]=0
            queue.append((i,j))

while queue:
    i,j=queue.popleft()

    if i+1<n and aux[i+1][j]>aux[i][j]+1:
        aux[i+1][j]=aux[i][j]+1
        queue.append((i+1,j))

    if j+1<m and aux[i][j+1]>aux[i][j]+1:
        aux[i][j+1]=aux[i][j]+1
        queue.append((i,j+1))

    if i-1>=0 and aux[i-1][j]>aux[i][j]+1:
        aux[i-1][j]=aux[i][j]+1
        queue.append((i-1,j))

    if j-1>=0 and aux[i][j-1]>aux[i][j]+1:
        aux[i][j-1]=aux[i][j]+1
        queue.append((i,j-1))

for i in range(n):
    for j in range(m):
        print(aux[i][j],end=" ")
    print()