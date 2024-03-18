import sqlite3

con = sqlite3.connect('teater.db')
cursor = con.cursor()

with open('skuespillereIStykke.sql', 'r') as file:
    result = cursor.execute(file.read())

for record in result:
    print(record)