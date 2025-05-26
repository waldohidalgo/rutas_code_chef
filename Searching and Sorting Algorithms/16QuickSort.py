def quick_sort(arr, low, high):
    # Write your code here

    if low>=high:
        return
    
    pivot=partition(arr,low,high)
    quick_sort(arr,low,pivot-1)
    quick_sort(arr,pivot+1,high)



def partition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            temp=arr[j]
            i+=1
            arr[j]=arr[i]
            arr[i]=temp
    i+=1
    temp=arr[i]
    arr[i]=pivot
    arr[high]=temp
    return i

arr=[9,8,7,6,5,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(arr)