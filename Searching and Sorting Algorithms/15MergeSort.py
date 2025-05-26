def merge(arr,l,m,r):
    l_a=[0]*(m+1-l)
    r_a=[0]*(r-m)
    for i in range(m+1-l):
        l_a[i]=arr[l+i]
    for j in range(r-m):
        r_a[j]=arr[m+1+j]
    i=j=0
    k=l
    while(i<(m+1-l) and j<(r-m)):
        if l_a[i]<r_a[j]:
            arr[k]=l_a[i]
            i+=1
        else:
            arr[k]=r_a[j]
            j+=1
        k+=1
    while i<(m+1-l):
        arr[k]=l_a[i]
        i+=1
        k+=1

    while j<(r-m):
        arr[k]=r_a[j]
        j+=1
        k+=1



def merge_sort(arr,l,r):
    if l==r:
        return
    mid=(l+r)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)
    merge(arr,l,mid,r)

arr=[6,5,3,1,8,7,2,4]
merge_sort(arr,0,len(arr)-1)
print(arr)