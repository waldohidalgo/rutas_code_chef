#!/c/Python312/python

# cook your dish here

n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))


j=0
found=None
while j<m and found is None:
    i=0
    while i<n:
        if matrix[i][j]!=0:
            found=i+1
            break
        i+=1
    j+=1
print(found)    
