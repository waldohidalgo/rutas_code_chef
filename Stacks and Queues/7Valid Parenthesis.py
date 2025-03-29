# cook your dish here
MAX_SIZE = 101
a = [''] * MAX_SIZE
top = -1

def push(ele):
    global top
    if top <= MAX_SIZE - 1:
        top += 1
        a[top] = ele
    else:
        print(f"Stack is full. Cannot push: {ele}")

def pop():
    global top
    if top >= 0:
        ele = a[top]
        top -= 1
        return ele
    else:
        print("Stack is empty. Cannot pop.")
        return '-1'

def is_empty():
    return top == -1

def is_full():
    return top >= MAX_SIZE

def is_matching_pair(open_char, close_char):
    return (open_char == '(' and close_char == ')')

def is_balanced(expression):
    # Write your code here
    for ch in expression:
        if ch=="(":
            push("(")
        else:
            if is_empty():
                return False
            if a[top]=="(":
                pop()
    return True if is_empty() else False
                

def main():
    t = int(input())

    while t > 0:
        expression = input()
        print(f"{expression} : {str(is_balanced(expression)).lower()}")
        t -= 1

if __name__ == "__main__":
    main()
