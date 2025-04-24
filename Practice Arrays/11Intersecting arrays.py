def intersect(nums1, nums2):
    # Write your code here
    
    ct1={}
    ct2={}
    for num in nums1:
        if num not in ct1:
            ct1[num]=1
        else:
            ct1[num]+=1
    for num in nums2:
        if num not in ct2:
            ct2[num]=1
        else:
            ct2[num]+=1
    res=[]
    for i in range(101):
        if i in ct1 and i in ct2:
            times=min(ct1[i],ct2[i])
            res.extend([i]*times)
    return res
    

def main():
    num1size, num2size = list(map(int, input().split()))
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    ans = intersect(nums1, nums2)
    print(*ans)

if __name__ == "__main__":
    main()