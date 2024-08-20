class Student:
    __age = None
    def __init__(self,age):
        self.__age = age

# Creating object of Student class
s = Student(20)
print(s.__age)