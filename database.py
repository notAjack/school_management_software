import sqlite3

school = sqlite3.connect("school.db")

curs = school.cursor()

curs.execute("SELECT * FROM students")
print(curs.fetchall())
school.commit()
school.close()