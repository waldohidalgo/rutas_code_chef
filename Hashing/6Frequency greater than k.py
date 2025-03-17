def main():
    k = 2
    s = "aaAbBcdDdD"
    
    # write your code here 
    res=[0]*(52)
    for ch in s:
        if ch.isupper():
            res[ord(ch)-65]+=1
        else:
            res[ord(ch)-97+26]+=1
    st=""        
    for i in range(52):
        if res[i]>=k:
            if i<26:
                st+=chr(i+65)
            else:
                st+=chr(i+97-26)
    print(st)


if __name__ == "__main__":
    main()