# I deleted the database file and rerun the code
import sqlite3
database = sqlite3.connect('app.db')
cursor = database.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS skills(name TEXT, progress TEXT, user_id INT)')
cursor.execute('CREATE TABLE IF NOT EXISTS users(user_id INT,name TEXT)')

# cursor.execute('INSERT INTO users(user_id,name ) VALUES(1,"Ahmed")')
# cursor.execute('INSERT INTO users(user_id,name ) VALUES(2,"Mohammed")')
# cursor.execute('INSERT INTO users(user_id,name ) VALUES(3,"Ali")')

# fetchone -> Returns a single record or None if no more rows are available
# fetchall -> Returns all the rows as a list -of tuples- of all the records, or an empty list if no rows are available
# fetchmany(size = num of returned rows) -> Returns a list of tuples of the remaining rows, or an empty list if no more rows are available

cursor.execute('SELECT * FROM users')
# print(cursor.fetchone()) # (1, 'Ahmed')
# print(cursor.fetchone()) # (2, 'Mohammed')
# print(cursor.fetchone()) #  (3, 'Ali')
# print(cursor.fetchone()) #  None

# print(cursor.fetchall()) # [(1, 'Ahmed'), (2, 'Mohammed'), (3, 'Ali')]
# print(cursor.fetchall()) # []

print(cursor.fetchmany(size=2)) # [(1, 'Ahmed'), (2, 'Mohammed')]
print(cursor.fetchmany(size=1)) # [(3, 'Ali')]



database.commit()
database.close()