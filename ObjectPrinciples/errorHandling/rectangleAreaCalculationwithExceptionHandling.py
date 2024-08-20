def is_valid_integer(value):
    if value.startswith('-'):
        value = value[1:]  # Remove the negative sign for further checking

    if value.isdigit():
        return True
    else:
        return False


try:
    length = input()
    width = input()
    
    if(is_valid_integer(length)==False or is_valid_integer(width)==False):
        # Complete the if block
        raise ValueError("Invalid Argument: Length and width must be integers.")
    
    length = int(length)
    width = int(width)
    
    if length < 0 or width < 0:
        # Complete the if block
        raise ValueError("Invalid Argument: Length and width must be positive values.")
        
    # Calculate the area of the rectangle
    area = length * width
    
    # Display the result
    print("Area:", area)
    
except ValueError as ve:
   # Print the error message
   print(ve)
    
except Exception as e:
    print("An unknown error occurred.")
    
finally:
    # Close the input stream
    pass
