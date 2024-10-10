from math import comb



for _ in range(int(input())):
    n,k=map(int,input().split())
    # se colocan k-1 separadores en n-1 espacios asegurando que se deja al menos 1 color
    result = comb(n-1, k-1)
    print(result)