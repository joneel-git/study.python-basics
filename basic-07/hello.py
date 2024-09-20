import keyboard
import time
#Keyboard input detection

y=1.0 # 1 second
x=0.1 

while True:
    key = keyboard.read_key()
    if key == "q":
        print(f"You pressed {key} Terminating...")
        time.sleep(y)
        print("...")
        break
    else:
        # Without time delay here i would get key printed twice why?
        print(key) # This is only run as long as you dont press Q
        time.sleep(x) # Add a small delay to prevent rapid printing
        continue