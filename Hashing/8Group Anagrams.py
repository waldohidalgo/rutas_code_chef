from collections import defaultdict

def hashing(string):
    arr=[0]*26
    for ch in string:
        arr[ord(ch)-97]+=1
    return ",".join(map(str,arr))

def group_anagrams(strings):
    # Complet this function
    hs=defaultdict(list)
    for string in strings:
        hs[hashing(string)].append(string)

    # for value in hs.values():
    #     print(value)
    return hs.values()

arr=["abc","dba","acb","bda","cba"]
print(group_anagrams(arr))
