#!/c/Python312/python

T=int(input())
arr=[tuple(map(int,input().split())) for _ in range(T)]

for l,r in arr:
    count=0
    residuoLeft=l%10
    residuoRight=r%10

    newLeft=l-residuoLeft
    newRight=r-residuoRight

    count=((newRight-newLeft)//10)*3
   
    if residuoLeft>=4:
        count-=2
    if residuoLeft==3:
        count-=1

    if residuoRight==2:
        count+=1
    if residuoRight>=3 and residuoRight<9:
        count+=2
    if residuoRight==9:
        count+=3
    print(count)
    
    
