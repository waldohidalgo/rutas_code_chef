#!/c/Python312/python

# cook your dish here
n=int(input())

matrix=[list(map(int,input().split())) for _ in range(n)]

directions=[(1,0),(0,1),(-1,0),(0,-1)]


limits=[n,n]
i=0
j=0
k=0
result=[]
while limits[0]>0 and limits[1]>0:
    for r in range(2):
        for c in range(limits[r]):
            result.append(matrix[i][j])
            if c==limits[r]-1:
                k=(k+1)%4
                limits[0],limits[1]=limits[0]-abs(directions[k][0]),limits[1]-abs(directions[k][1])      
            i,j=i+directions[k][0],j+directions[k][1]


    

print(result)
