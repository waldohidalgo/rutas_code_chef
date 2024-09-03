
# cook your dish here

# n,m=map(int,input().split())

# matrix=[list(map(int,input().split())) for _ in range(n)]

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]]

n=len(matrix)
m=len(matrix[0])

row,col=n,m
movements=[[0,1],[1,0],[0,-1],[-1,0]]
i,j=0,0
currentMovement=0
maxValues=[m,n]
while maxValues[0]>0 and maxValues[1]>0 :
    counts=[0,0]
    for k in range(2):
        while counts[k]<maxValues[k]:
            print(matrix[i][j],end=" ")
            counts[k]+=1
            if counts[k]==maxValues[k]:
                currentMovement=(currentMovement+1)%4
            i,j=i+movements[currentMovement][0],j+movements[currentMovement][1]
        maxValues=[maxValues[0]-abs(movements[currentMovement][1]),maxValues[1]-abs(movements[currentMovement][0])]
    

   

    


    
        

    
