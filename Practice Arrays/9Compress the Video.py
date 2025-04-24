t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    count=1
    for i in range(1,n):
        if a[i]!=a[i-1]:
            count+=1
    print(count)



