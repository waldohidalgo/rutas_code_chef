import copy
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Copy constructor
    def __copy__(self):
        print('hola')
        new_object = type(self)(self.attribute1, self.attribute2)
        return new_object

# Creating an object of MyClass
original_obj = MyClass("value1", "value2")

# Using the copy constructor to create a new object
#copied_obj = original_obj.__copy__()
secomd_copied_obj = copy.copy(original_obj)
print(secomd_copied_obj.attribute1)

# Displaying the attributes of the original and copied objects
#print("Original Object: attribute1={}, attribute2={}".format(original_obj.attribute1, original_obj.attribute2))
#print("Copied Object: attribute1={}, attribute2={}".format(copied_obj.attribute1, copied_obj.attribute2))