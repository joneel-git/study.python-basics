# A class named MyClass is created to represent an object.
# It has two pieces of information (attributes) that hold text.
# There are two functions (methods) that display this text when called.
# An instance of MyClass is created to use these functions.
# The functions are called to show the stored text.


class MyClass:  # Define a new class called MyClass
    def __init__(
        self,
    ):
        # self is a reference to the instance of the class itself
        # This is the initializer method that runs when we create an object
        self.instance_attribute = "I am an instance attribute that exists in function1"  # Create an instance attribute with a string value
        self.instance_attribute2 = "I am an instance attribute that exists in function2"

    def method(self):  # Define a method called function
        return print(
            self.instance_attribute
        )  # Return the value of the instance attribute

    def method2(self):
        return print(self.instance_attribute2)


obj = MyClass()  # Create an instance of MyClass and assign it to my_object
obj.method()  # Call the function method on my_object and print the result
obj.method2()  # Call the function2 method on my_object
