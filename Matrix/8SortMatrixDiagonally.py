#!/c/Python312/python

# cook your dish here


m,n=map(int,input().split())
matrix=[]
for i in range(m):
    matrix.append(list(map(int,input().split())))

def sortDiagonally(matrix):
    for k in range(n):
        i=0
        j=k
        temp=[]
        while i<m and j<n:
            temp.append(matrix[i][j])
            i+=1
            j+=1
        temp.sort()
        i=0
        j=k
        while i<m and j<n:
            matrix[i][j]=temp[i]
            i+=1
            j+=1

    for k in range(1,m):
        i=k
        j=0
        temp=[]
        while i<m and j<n:
            temp.append(matrix[i][j])
            i+=1
            j+=1
        temp.sort()
        i=k
        j=0
        while i<m and j<n:
            matrix[i][j]=temp[j]
            i+=1
            j+=1
    print("----")
    for i in range(m):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

sortDiagonally(matrix)
