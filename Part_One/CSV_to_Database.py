# Add the rows of the text file to the Database file
import sqlite3
import pandas

data = pandas.read_csv("CSV_to_Database.txt")

connection = sqlite3.connect("Database_Filter.db")
cursor = connection.cursor()
for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cursor.execute("INSERT INTO countries VALUES(NULL, ?, ?, NULL)",(row["Country"], row["Area"]))
    connection.commit()
    connection.close()
