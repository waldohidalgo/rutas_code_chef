def counting_sort(arr):
    if not arr:
        return
    max_val=max(arr)
    min_val=min(arr)
    width=max_val-min_val+1
    count=[0]*(width)

    for el in arr:
        index=el-min_val
        count[index]+=1
    
    for i in range(1,width):
        count[i]+=count[i-1]
    print(count)
    n=len(arr)
    res=[0]*(n)
    
    for i in range(n-1,-1,-1):
        num=arr[i]
        index=num-min_val
        count[index]-=1
        res[count[index]]=num
    return res
    
arr=[4,2,2,8,3,3,1]
print(counting_sort(arr))

