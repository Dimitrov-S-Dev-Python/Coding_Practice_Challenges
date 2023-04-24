# From Database_Filter.db
# select country that have an area grater than 2_000_000
# then export those rows to a CSV file
import sqlite3
import pandas

connection = sqlite3.connect("Database_Filter.db")
cursor = connection.cursor()
cursor.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()
connection.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("Countries_big_Area.csv", index=False)