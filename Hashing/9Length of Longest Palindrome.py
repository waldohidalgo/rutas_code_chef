from collections import Counter
def longest_palindrome_length(s: str) -> int:
    
    # Count frequency of each character
    hs=Counter(s)
    #Write your code here
    ct=0
    exist_impar=False
    for key in hs:
        if not key.isalpha():
            continue
        elem=hs[key]
        if elem%2==0:
            ct+=elem
        else:
            ct+=elem-1
            if not exist_impar:
                exist_impar=True
    return ct+exist_impar

# from a import s
# print(Counter(s))
s="abcdabbbb"
print(longest_palindrome_length(s))