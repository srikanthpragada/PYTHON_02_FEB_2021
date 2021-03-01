import sqlite3

con = sqlite3.connect(r"d:\classroom\feb2\hr.db")
print(type(con))
cur = con.cursor()
print(type(cur))

con.close()