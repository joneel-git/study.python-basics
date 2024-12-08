import mysql.connector

# Step 1 — Establish a connection to the database:
# You can establish a connection to a MySQL database using the connect( )
mydb = mysql.connector.connect(user="root", password="1234")
# Create a cursor object: A cursor is a temporary storage area in a
# database management system
cursor = mydb.cursor()

# Create a database: To create a database, you can execute the SQL
# cursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

database_exists = False
for database in databases:
    if "mydatabase" in database:
        database_exists = True
        break

if database_exists:
    print("Database exists")
    for x in databases:
        print(x)
else:
    print("Database does not exist")
