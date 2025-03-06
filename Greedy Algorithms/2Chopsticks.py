n,d=list(map(int,input().split()))
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
i=0
ct=0
while i<n-1:
    if arr[i+1]-arr[i]<=d:
        ct+=1
        i+=2
    else:
        i+=1

print(ct) 
