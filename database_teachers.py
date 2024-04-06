import sqlite3

school = sqlite3.connect("school.db")

curs = school.cursor()

curs.execute("""CREATE TABLE teachers (
        teach_id integer PRIMARY KEY AUTOINCREMENT,
        teach_name text,
        subject text,
        class_teacher_of text
    )""")

#curs.execute("INSERT INTO teachers VALUES ('1', 'teacher1', 'maths', '10')")
print(curs.fetchall())
school.commit()
school.close()