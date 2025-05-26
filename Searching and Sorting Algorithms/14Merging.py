n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

i,j,k=0,0,0
arr3=[0]*(n+m)
while i<n and j<m:
    if arr1[i]<arr2[j]:
        arr3[k]=arr1[i]
        i+=1
    else:
        arr3[k]=arr2[j]
        j+=1
    k+=1

while i<n:
    arr3[k]=arr1[i]
    i+=1
    k+=1

while j<m:
    arr3[k]=arr2[j]
    j+=1
    k+=1

print(*arr3)