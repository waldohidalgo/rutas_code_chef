#!/c/Python312/python

# cook your dish here

n,m,x=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]

# n,m,x=2,4,0
# matrix=[[1],[5]]
index=-1
start=0
end=n-1
while start<=end:
    mid=start + (end+1-start)//2
    if matrix[mid][0]==x:
        index=mid
        break
    if start==end:
        index=start
        break
    elif matrix[mid][0]>x:
        end=mid - 1 
    else:
        start=mid

if index==-1:
    print("NO")
else:
    arr=matrix[index]
    isFound=False
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start + (end+1-start)//2
        if arr[mid]==x:
            isFound=True
            break
        if start==end:
            break
        elif arr[mid]>x:
            end=mid - 1
        else:
            start=mid
    if isFound:
        print("YES")
    else:
        print("NO")
