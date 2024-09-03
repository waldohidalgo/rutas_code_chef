#!/c/Python312/python



# cook your dish here

n=int(input())

matrix=[list(map(int,input().split())) for _ in range(n)]

def maxSquare(i,j,matrix,n):
    maxCount=1 if matrix[i][j]==1 else 0
    isSquare=True if matrix[i][j]==1 else False
    k=1
    while isSquare and i+k<=n and j+k<=n:
        i1=i
        while i1<n and i1<i+k and isSquare:
            j1=j
            while j1<n and j1<j+k and isSquare:
                if matrix[i1][j1]==0:
                    isSquare=False
                j1+=1
            i1+=1
        if not isSquare:
            break
        maxCount=max(maxCount,k)
        k+=1
    return maxCount

maxSquareMatrix=0
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            maxSquareMatrix=max(maxSquareMatrix,maxSquare(i,j,matrix,n))
            
print(maxSquareMatrix**2)
            
                