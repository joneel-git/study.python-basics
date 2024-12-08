import customtkinter as ctk

# Sets the appearence mode of the application
# System has the same appearance same as the system.
ctk.set_appearance_mode("system")

# The default color of the widget 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Sets the title of our window to "App"
        # All we done so far is just displaying a title and 
        # Giving height and width of the app
        self.title("App")
        # Dimensions of the window will be 200x200
        self.geometry("200x200")

if __name__ == "__main__":
    app = App()
    # This runs the app
    app.mainloop()
