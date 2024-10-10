# cook your dish here
val=10**9+7

factorial_memo={}
def factorial(n):
    if n in factorial_memo:
        return factorial_memo[n]
    if n == 0:
        return 1
    else:
        factorial_memo[n] = n * factorial(n - 1) % val
        return factorial_memo[n]
    
for _ in range(int(input())):
    n,k=map(int,input().split())

    if n>k:
        res=factorial(k)
    if n<=k:
        res=(factorial(k)*pow(factorial(k-n),val-2,val))%val

    print(res)