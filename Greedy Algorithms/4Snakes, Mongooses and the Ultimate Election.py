t=int(input())
result={0:"mongooses",1:"snakes",2:"tie"}
for _ in range(t):
    s=input()
    arr=list(s)
    n=len(s)
    ct_mongooses=0
    for i in range(n):
        if arr[i]=="m":
            ct_mongooses+=1
            if i-1>=0 and arr[i-1]=="s":
                arr[i-1]=""
            elif i+1<n and arr[i+1]=="s":
                arr[i+1]=""
    
    ct_snakes=len("".join(arr))-ct_mongooses
    if ct_snakes>ct_mongooses:
        print(result[1])
    elif ct_snakes<ct_mongooses:
        print(result[0])
    else:
        print(result[2])

            