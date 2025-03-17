def subarray_sum(nums, k):
    #Write your code here
    n=len(nums)
    hs={0:1}
    acum=0
    ct=0
    for i in range(n):
        acum+=nums[i]
        if acum-k in hs:
            ct+=hs[acum-k]

        hs[acum]=hs.get(acum,0)+1
    return ct

arr=[1,1,0,0,0,0,1,0,1]
k=2
print(subarray_sum(arr,k))