import os
def user_function():
    # Define the directory path
    directory_path = "./HandleFiles"

    # List the files and directories inside "/mnt/codechef"
    files = os.listdir(directory_path)

    # Check if there are any files or directories
    if files:
        # Iterate through each file or directory and print its name
        for file_name in files:
            print(file_name)

def readFile():
    filename = "./HandleFiles/file.txt"
    try:
        with open(filename, 'r') as my_file:
            for line in my_file:
                print(line.rstrip())
    except FileNotFoundError as e:
        print(e)


readFile()