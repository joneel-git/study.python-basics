class MyClass:
    def __init__(self):
        self.value = None  # Initialize the attribute

    def set_value(self, string):
        self.value = string  # Set the value of the attribute

    def get_value(self):
        return self.value  # Return the value of the attribute


# Create an instance of MyClass
instance = MyClass()

# Set the attribute using the setter method
instance.set_value("Hello World")

# Get the attribute using the getter method
value = instance.get_value()

# Print the retrieved value
print(value)  # This will output: Hello World
