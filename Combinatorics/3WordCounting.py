val = 10**9 + 7

factorial_memo={}
def factorial(n):
    if n in factorial_memo:
        return factorial_memo[n]
    if n == 0:
        return 1
    else:
        factorial_memo[n] = n * factorial(n - 1) % val
        return factorial_memo[n]
    

t = int(input())
for _ in range(t):
    s = input()
    diccionario = {i:diccionario.get(i,0) + 1 for i in s}
    

    factorial_s = factorial(len(s))
    factorial_veces = 1
    for count in diccionario.values():
        factorial_veces = (factorial_veces * factorial(count)) % val

    
    # Aplicación del pequeño teorema de fermat
    res = (factorial_s * pow(factorial_veces, val - 2, val)) % val
    print(res)