t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    total_without_discount=0
    total_with_discount=x
    for el in a:
        total_without_discount+=el
        total_with_discount+=(el-y) if (el-y>=0) else 0
    if(total_with_discount<total_without_discount):
        print("COUPON")
    else:
        print("NO COUPON")
