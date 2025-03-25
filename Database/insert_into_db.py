import sqlite3

# Cursor -> It is a pointer to the database, and it is used to execute the SQL queries
# Any operation on the database is done through the cursor

# commit() -> Save (commit) all changes

# Creating a Connection, and a Database named `book`
database = sqlite3.connect('app.db')

cursor = database.cursor()

# Creating a Table named `skills` and its columns
cursor.execute('CREATE TABLE IF NOT EXISTS skills(name TEXT, progress TEXT, user_id INT)')

# Creating a Table named `users` and its columns
cursor.execute('CREATE TABLE IF NOT EXISTS users(user_id INT,name TEXT)')

# Inserting data into users table

cursor.execute('INSERT INTO users(user_id,name ) VALUES(1,"Ahmed")')
cursor.execute('INSERT INTO users(user_id,name ) VALUES(2,"Mohammed")')
cursor.execute('INSERT INTO users(user_id,name ) VALUES(3,"Ali")')

# Save (commit) all changes
database.commit()

# Close the connection
database.close()