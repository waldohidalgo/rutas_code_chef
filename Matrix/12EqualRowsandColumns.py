#!/c/Python312/python

# cook your dish here


n=int(input())

matrix=[tuple(map(int,input().split())) for _ in range(n)]

colums=[tuple(matrix[i][j] for i in range(n)) for j in range(n)]


count=0
for row in matrix:
    for col in colums:
        if row==col:
            count+=1
print(count)




# Metodo 1

# n=int(input())

# matrix=[]

# for i in range(n):
#     matrix.append(list(map(int,input().split())))


# count=0
# for k in range(n):
#     row=matrix[k]
#     j=0
#     while j < n:
#         isEqual=True
#         i=0
#         while i < n and isEqual:
#             if row[i]!=matrix[i][j]:
#                 isEqual=False
#             i+=1
#         if isEqual:
#             count+=1
#         j+=1

# print(count)

