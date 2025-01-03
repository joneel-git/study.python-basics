class Myclass:
    def __init__(self, name):
        self.somestring = name

    # Instance method
    def get_string(self):
        return self.somestring

def create_string_object():
    myobject = Myclass("name")
    myobject2 = Myclass("name2")
    instance_object = f"{myobject.get_string()} {myobject2.get_string()}"
    return instance_object

print(create_string_object())