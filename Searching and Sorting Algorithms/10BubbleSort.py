def bubble_sort(arr):
    # Write your code here
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]    