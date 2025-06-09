t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # your code goes here
    max_comments=0
    max_val=0
    position=0
    for index,value in enumerate(a):
        if value>max_val:
            max_val=value
            max_comments=b[index]
            position=index+1
        elif value==max_val:
            if b[index]>b[position-1]:
                max_comments=b[index]
                position=index+1
    print(position)
