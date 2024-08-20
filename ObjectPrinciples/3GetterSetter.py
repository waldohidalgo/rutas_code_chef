class MyClass :
    __myField = None
    
    # Getter method for myField
    def getMyField(self): 
        return MyClass.__myField

    # Setter method for myField
    def setMyField(self , value): 
        MyClass.__myField = value


obj = MyClass()
# Using the setter method to set the value of myField
obj.setMyField(42)
# Using the getter method to retrieve the value of myField
value = obj.getMyField()
print("Value of myField: ", value)
