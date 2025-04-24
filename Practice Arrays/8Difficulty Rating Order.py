t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    for i in range(1,n):
        if d[i-1]>d[i]:
            print("No")
            break
    else:
        print("Yes")


