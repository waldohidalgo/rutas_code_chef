class Student:
    def __init__(self, student_name, student_score):
        self.name = student_name
        self.score = student_score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score


try:
    # Create a Student object with predefined values
    student = Student("Alice", -90)
    
    try:
        # Check if the student's score is within the valid range (0-100)
        if student.get_score() < 0 or student.get_score() > 100:
            raise ValueError("Invalid score.")
            
        # Display student information if the score is valid
        print("Student Name:", student.get_name())
        print("Student Score:", student.get_score())
        
    except ValueError as e:
        # Handle specific exception (Invalid score)
                
except Exception as e:
    # Handle any other unknown exceptions
    print("An unknown error occurred.")


