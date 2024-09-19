#!/c/Python312/python
# cook your dish here
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
q=int(input())
matrices=[[[0]*(n+1) for _ in range(n+1)] for _ in range(11)]

for k in range(1,11):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==k:
                matrices[k][i+1][j+1]=1
    ## calculo de prefix count en la mismas matrices 
    for i in range(n):
        for j in range(n):
            matrices[k][i+1][j+1]+=matrices[k][i][j+1]+matrices[k][i+1][j]-matrices[k][i][j]
for query in range(q):
    x1,y1,x2,y2=map(int,input().split())
    count=0
    for k in range(1,11):
        if matrices[k][x2][y2]-matrices[k][x2][y1-1]-matrices[k][x1-1][y2]+matrices[k][x1-1][y1-1]>0:
            count+=1
    print(count)
       
            
    