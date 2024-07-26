# A variable is a reusable container for storing a value
# A variable behaves as if it were the value it contains

# INTEGER
# An integer is a whole number without a decimal point
age = 21  # Example: Your age
players = 2  # Example: Number of players online
quantity = 5  # Example: Quantity of items to buy

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# FLOAT
# A float is a number that includes a decimal point
gpa = 3.2  # Example: Grade point average
distance = 2.5  # Example: Distance ran in kilometers
price = 10.99  # Example: Price in dollars

print(f"\nYour GPA is {gpa}")
print(f"You ran {distance} Km")
print(f"The price is ${price}")


# STRING
# A string is a sequence of characters, like words or sentences
name = "dude bro"  # Example: A person's name
food = "Pizza"  # Example: A favorite food
email = "random@email.com"  # Example: An email address

print(f"\nYour name is {name}")
print(f"My favorite food is {food}")
print(f"My email is {email}")


# BOOLEAN
# A boolean is like a light switch, it can be either on (True) or off (False)
# It represents whether something is happening or not

online = True  # Example: Whether you are online
for_sale = True  # Example: Whether an item is for sale
running = False  # Example: Whether a process is running

print(f"\nAre you online?: {online}")
print(f"Is this item for sale?: {for_sale}")
print(f"Is the game running?: {running}")

# IF STATEMENT
# An if statement checks a condition and decides what to do next based on whether the condition is True or False
# It's like asking a question: "Is the game running?"
if running:
    print("\nThe game is running")
else:
    print("\nThe game is over..")
