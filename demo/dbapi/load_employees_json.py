import sqlite3
import json

con = sqlite3.connect(r"d:\classroom\feb2\hr.db")
cur = con.cursor()
f = open("employees.json","rt")
employees = json.load(f)
count = 0
for e in employees:
    try:
        cur.execute("insert into employees(name,job,salary) values(?,?,?)",
                    (e['name'], e['job'], e['salary']))
        count += 1
    except Exception as ex:
        print(ex)

con.commit()
f.close()
print(f"Loaded {count} employees!")
cur.close()
con.close()

