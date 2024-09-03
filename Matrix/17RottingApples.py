#!/c/Python312/python
# cook your dish here
from collections import deque

n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]

def bfs(q,matrix):
    time=0
    while q:
        for _ in range(len(q)):
            i,j=q.popleft()

            if i+1<n and matrix[i+1][j]==1:
                matrix[i+1][j]=2
                q.append((i+1,j))

            if j+1<m and matrix[i][j+1]==1:
                matrix[i][j+1]=2
                q.append((i,j+1))

            if i-1>=0 and matrix[i-1][j]==1:
                matrix[i-1][j]=2
                q.append((i-1,j))

            if j-1>=0 and matrix[i][j-1]==1:
                matrix[i][j-1]=2
                q.append((i,j-1))

        time+=1
    return time-1



q=deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j]==2:
            q.append((i,j))

minRotting=bfs(q,matrix)

for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            minRotting=-1
            break

print(minRotting)