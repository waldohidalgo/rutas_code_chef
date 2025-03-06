t=int(input())
for _ in range(t):
    n=int(input())
    sequences=[]
    for _ in range(n):
        sequence=list(map(int,input().split()))
        sequence.sort(reverse=True)
        sequences.append(sequence)
    sequences.reverse()
    max_sum=[]
    max_elem=float("inf")
    for i in range(n):
        sequence=sequences[i]
        for j in range(len(sequence)):
            if sequence[j]<max_elem:
                max_sum.append(sequence[j])
                max_elem=sequence[j]
                break
        if len(max_sum)!=(i+1):
            print(-1)
            break
    else:
        print(sum(max_sum))




    