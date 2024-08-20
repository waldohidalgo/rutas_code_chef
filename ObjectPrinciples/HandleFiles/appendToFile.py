
def user_function():
    file = "./HandleFiles/input.txt"
    try:
        # Open file in append mode
        
        with open(file,"a") as inputFile:
            inputFile.write("5\n")
            inputFile.write("10\n")
            inputFile.write("abcd\n")
            inputFile.write("11\n")
            inputFile.write("12.0\n")     
        
    except IOError as e:
        print(e)

    # Display the contents of input.txt
    try:
        with open(file,"r") as inputFile:
            for line in inputFile:
                print(line.rstrip())
        
        
    except IOError as e:
        print("Error displaying file contents:", e)



user_function()

