import sqlite3


connection = sqlite3.connect("buttsmell.db")
cursor = connection.cursor()
cursor.execute("create table smellbutt (last_meal text, time integer, hours_since_poo integer, stink_level integer)")

stink_level = [
    ("burger", 12, 24, 34),
    ("thai curry", 12, 34, 99),
    ("bad hot dog", 3, 34, 99),
    ("macaroni", 12, 24, 99),
    ("cheese", 12, 24, 99),
    ("cheeseburger", 12, 24, 99),
]

cursor.executemany("insert into smellbutt values (?,?,?,?)", stink_level)

for row in cursor.execute("select * from smellbutt"):
    print(row)

connection.close()