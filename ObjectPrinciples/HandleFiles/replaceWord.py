import re
def user_function():
    # Define the input file path
    file_path = "./input.txt"

    try:
        # Read the content of the input file
        with open(file_path, 'r') as file:
            content = file.read()

        # Define the search and replace strings
        search = "Codechef"
        replace = "CodeChef"

        # Replace occurrences of search string with replace string
        modified_content = re.sub(search, replace, content)
        

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        # Display the modified file contents
        with open(file_path, 'r') as file:
            for line in file:
                print(line.rstrip())
        

    except IOError as e:
        print("An error occurred:", e)



user_function()