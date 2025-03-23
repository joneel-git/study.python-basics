import os

class MyClass:
    def __init__(self):
        cwd = os.getcwd() # used to get the current working directory
        self.currentdir = os.path.join(cwd, "folder")  # Set the folder name here

    def path_exists(self):
        folder = self.currentdir  # Use the current directory set in __init__

        for filename in os.listdir(folder):
            infilename = os.path.join(folder, filename)
            if not os.path.isfile(infilename):
                continue
            
            # Change extension to .mp3 if not already .mp3
            if not filename.endswith('.mp3'):
                newname = os.path.splitext(infilename)[0] + '.mp3'
                os.rename(infilename, newname)

# Example usage:
c = MyClass()  # Create an instance of MyClass
c.path_exists()  # Call the method without any arguments
