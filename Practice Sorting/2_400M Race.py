t = int(input())
for _ in range(t):
    arr= list(map(int, input().split()))
    # your code goes here
    names=["ALICE","BOB","CHARLIE"]
    min_index=0
    for i,e in enumerate(arr):
        if e<arr[min_index]:
            min_index=i
    print(names[min_index])