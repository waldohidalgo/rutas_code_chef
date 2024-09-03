#!/c/Python312/python

n,m=map(int,input().split())

matrix=[list(map(int,input().split())) for _ in range(n)]


minValue=min([matrix[i][0] for i in range(n)])
maxValue=max([matrix[i][m-1] for i in range(n)])

def countLessEqual(matrix, midValue):
    count=0
    for i in range(n):
        j=0
        while j<m and matrix[i][j]<=midValue:
            j+=1
        count+=j
    return count

while minValue<maxValue:
    midValue=(minValue+maxValue)//2
    lessEqual=countLessEqual(matrix, midValue)
    if lessEqual<=(n*m)//2:
        minValue=midValue+1
    else:
        maxValue=midValue

print(minValue)                                                        
    


# def countLessEqual(matrix, midValue):
#     count=0
#     for i in range(n):
#         l=0
#         r=m-1
#         while l<=r:
#             mid=(l+r)//2
#             if matrix[i][mid]<=midValue:
#                 l=mid+1
#             else:
#                 r=mid-1
#         count+=l
#     return count