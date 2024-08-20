class Student:
    class Course:
        def __init__(self):
            self.course_name = ""

        def set_data(self, course_name):
            self.course_name = course_name

        def display(self):
            print(self.course_name)

    def __init__(self, name, course_name):
        self.name = name
        self.course = self.Course()
        self.course.set_data(course_name)

    def display(self):
        print(self.name)
        self.course.display()


# Take inputs
a,b=input().split()

# Create a student and a course
student=Student(a,b)

# Display student's name and course name
student.display()
