n=int(input())
arr=list(map(int,input().split()))
minimun,maximun=float("inf"),float("-inf")
for num in arr:
    if minimun>num:
        minimun=num
    if maximun<num:
        maximun=num
        
print(minimun,maximun)