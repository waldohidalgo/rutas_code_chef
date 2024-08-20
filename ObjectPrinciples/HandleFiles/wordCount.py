import re
def user_function():
    file = "./HandleFiles/input.txt"
    try:
        with open(file, 'r') as my_file:
            cnt = 0
            for line in my_file:
                onlineLetter=re.findall(r"\w+",line)
                cnt += len(onlineLetter)
            print("Number of words:", cnt)
    except FileNotFoundError as e:
        print(e)


user_function()