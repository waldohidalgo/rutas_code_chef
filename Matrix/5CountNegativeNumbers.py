#!/c/Python312/python


n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))


i=0
j=m-1
count=0
while i<n and j>=0:
    if matrix[i][j]<0:
        count+=n-i
        j-=1
    else:
        i+=1
print(count)