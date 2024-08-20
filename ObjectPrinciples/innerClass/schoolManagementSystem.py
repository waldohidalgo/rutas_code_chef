class School:
    class Student:
        def __init__(self, name):
            self.name = name

        def display(self):
            print(self.name)

    def __init__(self, school_name, student):
        self.school_name = school_name
        self.student = student

    def display_school_info(self):
        print(self.school_name)
        self.student.display()


student = School.Student("Alice")
school = School("ABC School", student)

school.display_school_info()
