t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    max_streak_a,count_a=0,0
    max_streak_b,count_b=0,0
    for i in range(n):
        if a[i]>0:
            count_a+=1
        else:
            count_a=0
        max_streak_a=max(max_streak_a,count_a)


        if b[i]>0:
            count_b+=1
        else:
            count_b=0
        max_streak_b=max(max_streak_b,count_b)     

    if max_streak_a>max_streak_b:
        print("OM")   
    elif max_streak_a<max_streak_b:
        print("ADDY")
    else:
        print("DRAW")