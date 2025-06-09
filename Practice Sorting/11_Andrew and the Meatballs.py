t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    # your code goes here
    p.sort(reverse=True)
    count_plates=0
    count_meatballs=0
    for i in range(n):
        count_meatballs+=p[i]
        count_plates+=1
        if count_meatballs>=m:
            print(count_plates)
            break
    else:
        print(-1)