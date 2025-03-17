from collections import Counter

def get_window_substring(s1,s2):
    n=len(s1)
    m=len(s2)
    ct=Counter()
    target=Counter(s2)

    if n<m:
        return -1
    left=0
    min_len=float("inf")
    min_left=-1
    formed=0
    for i in range(n):
        ct[s1[i]]+=1

        if s1[i] in target and ct[s1[i]]==target[s1[i]]:
            formed+=1
        # desde afuera hacia adentro ya que keys en target también
        # pueden estar dentro del substring
        while formed==len(target):
            if i-left+1<min_len:
                min_len=i-left+1
                min_left=left  

            if s1[left] in target and ct[s1[left]]==target[s1[left]]:
                formed-=1
            ct[s1[left]]-=1
            left+=1

    return s1[min_left:min_left+min_len] if min_left!=-1 else -1
    
#s1,s2="AABCBBAC","ABC"
#s1,s2="cccdafabca","ca"
#s1,s2 = "ADOfffffBECODEBANerereC", "ABC"
#s1,s2="abbacfffa","aabc"
#s1,s2="badccacbcb","acbc"
#s1,s2="c","a"
s1,s2="aaabccddabe","abcdd"
print(get_window_substring(s1,s2))
