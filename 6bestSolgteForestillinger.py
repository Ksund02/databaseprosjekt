import sqlite3

con = sqlite3.connect('teater.db')
cursor = con.cursor()

with open('bestSolgteForestillinger.sql', 'r') as file:
    result = cursor.execute(file.read())

result = cursor.fetchall()
for row in result:
    print(row)

con.close()