def convert_to_rpn(s:str):
    operators=[]
    res=""
    for i in s:
        if i=="(":
            continue

        if i==")":
            res+=operators.pop()
        elif i.isalpha():
            res+=i
        else:
            operators.append(i)
    return res

#print(convert_to_rpn("((a+t)*((b+(a+c))^(c+d)))"))