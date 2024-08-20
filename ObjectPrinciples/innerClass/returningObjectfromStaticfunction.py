class Name:
    def __init__(self):
        self.name = None  # Data member to store a name

    @staticmethod
    def concatenate_names(obj1, obj2):
        # Create a new Name object and set its name data member to the concatenated result
        result = Name()
        result.name = obj1.name + " " + obj2.name
        return result



# Create an instance of the Name class and set the name data member
name1 = Name()
name1.name = "Tom"

# Create another instance of the Name class and set the name data member
name2 = Name()
name2.name = "Jerry"

# Use the concatenate_names static method to concatenate the names
concatenated_name = Name.concatenate_names(name1, name2)
# Display the concatenated name using the name data member of the result
print(concatenated_name.name)

