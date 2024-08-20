def user_function():
    # Open files in respective modes
    input_filename = "./HandleFiles/input.txt"
    output_filename = "./HandleFiles/output.txt"
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            # Read and write the numbers from the file
            for line in input_file:
                output_file.write(line)

        # Display the contents of output.txt
        with open(output_filename, 'r') as output_file:
            for line in output_file:
                print(line.strip())
    except IOError as e:
        print("I/O error:", e)


user_function()
