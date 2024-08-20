class OuterClass:
    def __init__(self, outer_attr):
        self.outer_attr = outer_attr

    def outer_method(self):
        print("This is an outer method.")

    class InnerClass:
        def __init__(self, inner_attr):
            self.inner_attr = inner_attr

        def inner_method(self):
            print("This is an inner method.")

# Creating an instance of the outer class
outer_instance = OuterClass(outer_attr="Outer Attribute")

# Creating an instance of the inner class using the outer class instance
inner_instance = outer_instance.InnerClass(inner_attr="Inner Attribute")

# Accessing attributes and methods
print(outer_instance.outer_attr)  # Output: Outer Attribute
outer_instance.outer_method()      # Output: This is an outer method.

print(inner_instance.inner_attr)  # Output: Inner Attribute
inner_instance.inner_method()      # Output: This is an inner method.
