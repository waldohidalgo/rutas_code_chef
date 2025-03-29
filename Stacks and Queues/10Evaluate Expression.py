def evaluate_exp(s:str):
    numbers=[]
    for i in s:
        if i.isdigit():
            numbers.append(i)
        else:
            b=int(numbers.pop())
            a=int(numbers.pop())
            if i=="+":
                numbers.append(a+b)
            elif i=="-":
                numbers.append(a-b)
            else:
                # *
                numbers.append(a*b)
    return numbers[0]

print(evaluate_exp("703*-9-"))