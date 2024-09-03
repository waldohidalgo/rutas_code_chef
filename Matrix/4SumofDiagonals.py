#!/c/Python312/python

n=int(input())

matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

def method1(matrix):
    sum=0
    for i in range(n):
        if i!=n-i-1:
            sum+=matrix[i][i]+matrix[i][n-i-1]
        else:
            sum+=matrix[i][i]

    print(sum)

def method2(matrix):
    sum=0
    i=0
    j=n-1
    while i<n and j>=0:
        if i!=j:
            sum+=matrix[i][i]+matrix[i][j]
        else:
            sum+=matrix[i][i]
        i+=1
        j-=1
    print(sum)


method2(matrix)