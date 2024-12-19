import modules
from tinydb import TinyDB, Query

# modules.greeting("john")

"""
To locate or to access data..
Find the index of a value in a sequense 
"""

db = TinyDB(".dbjson")
User = Query()


def add_user():
    user = db.insert({"id": 1, "name": "John", "age": 22})
    user = db.insert({"id": 2, "name": "Maria", "age": 21})
    print(f"We added new user {user}")


def delete_user():
    deleted_user = db.remove(User.id == 1)
    print(f"Removing the user {deleted_user}")

def show_users():
    show_the_users = db.all()
    print(f"{show_the_users}")

# Call the functions to execute them
# add_user()      # Add users to the database
# show_users()    # Show all users
# delete_user()   # Delete a user
show_users()    # Show users again to see the changes
# print("after removing john we have: ", result)
