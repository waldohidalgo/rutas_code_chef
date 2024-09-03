#!/c/Python312/python

# cook your dish here
n=int(input())

matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for i in range(n):
    count=0
    for j in range(n):     
        if count<n:
            if j!=n-1-j:
                count+=2
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
            else:
                count+=1
            

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
