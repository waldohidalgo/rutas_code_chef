from abc import ABC, abstractmethod

class TextFormatter(ABC):
    @abstractmethod
    def format(self, text):
        pass

class UpperCaseFormatter(TextFormatter):
    # Write your code here
    def format(self, text):
        return text.upper()
    

class ReverseFormatter(TextFormatter):
    # Write your code here
    def format(self, text):
        return text[::-1]
    


text = "Codechef"

# Format the text using UpperCaseFormatter
formatter = UpperCaseFormatter()
print(formatter.format(text))

# Format the text using ReverseFormatter
formatter = ReverseFormatter()
print(formatter.format(text))
