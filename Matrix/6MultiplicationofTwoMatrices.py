#!/c/Python312/python
# cook your dish here
n1,m1=map(int,input().split())
matrix1=[]
for i in range(n1):
    matrix1.append(list(map(int,input().split())))
n2,m2=map(int,input().split())
matrix2=[]
for i in range(n2):
    matrix2.append(list(map(int,input().split())))

res=[[0 for j in range(m2)] for i in range(n1)]

for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            res[i][j]+=matrix1[i][k]*matrix2[k][j]

for i in range(n1):
    for j in range(m2):
        print(res[i][j],end=" ")
    print()
        
            