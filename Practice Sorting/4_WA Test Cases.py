t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    v = input()
    min_val=None
    # your code goes here
    for index,value in enumerate(v):
        if value=="0":
            if min_val is None:
                min_val=s[index]
            else:
                if min_val>s[index]:
                    min_val=s[index]
    print(min_val)