import sqlite3

school = sqlite3.connect("school.db")

curs = school.cursor()

curs.execute("""CREATE TABLE teachers (
        teach_id integer PRIMARY KEY AUTOINCREMENT,
        teacher_name text,
        subject text,
        class_teacher_of text
    )""")

school.commit()
school.close()