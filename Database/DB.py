# Importing the sqlite3 module
import sqlite3

# Creating a Connection, and a Database named `book`
database = sqlite3.connect('app.db')
# Creating a Table named `skills` and its columns
database.execute('CREATE TABLE IF NOT EXISTS skills(name TEXT, progress TEXT, user_id INT)')

# Close the connection
# database.close()


