t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    first_max=0
    second_max=0
    for i in range(n):
        if a[i]>first_max:
            second_max=first_max
            first_max=a[i]
        elif a[i]!=first_max and a[i]>second_max:
            second_max=a[i]
    print(first_max+second_max)
            
