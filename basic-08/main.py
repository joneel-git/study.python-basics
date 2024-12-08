# https://www.youtube.com/watch?v=MvzK9Oguxcg  Watch this for references
import customtkinter as ctk

# Sets the appearence mode of the application
# System has the same appearance same as the system.
ctk.set_appearance_mode("system")

# The default color of the widget 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self):
        super().__init__()  # Call the parent class's constructor

        # when you create a label (or any other widget) inside a class, 
        # you use self to refer to the instance of that class. 
        # This allows you to access the label later if you need to update it 
        # or manipulate it in some way.
        
        # Sets the title of our window to "App"
        # All we done so far is just displaying a title and 
        # Giving height and width of the app
        self.title("App")  # Use self to refer to the current instance
        # Dimensions of the window will be 200x200
        self.geometry("200x200")

        # Example of making a label in this code base
        self.label = ctk.CTkLabel(
            self, text="Hello self as root label"
        )
        self.label.pack(pady=20, padx=20)

if __name__ == "__main__":
    app = App()
    # This runs the app
    app.mainloop()
