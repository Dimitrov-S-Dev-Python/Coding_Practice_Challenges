# Print out those countries from Database_Filter.db
# that have an area grater than 2_000_000
import sqlite3

connection = sqlite3.connect("Database_Filter.db")
cursor = connection.cursor()
cursor.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()
connection.close()
for country in rows:
    print(country[0])
