
import re

def user_function():
    file_path = "./input.txt"
    try:
        with open(file_path, 'r') as file:
            search = r"CodeChef\b"
            cnt = 0
            # Count the number of occurrences of the word - "CodeChef" in the file input.txt
            for line in file:
                cnt += len(re.findall(search, line))

        
        
        
        print("Number of occurrences of 'CodeChef':", cnt)
    except IOError as e:
        print("Error reading the file:", e)

user_function()