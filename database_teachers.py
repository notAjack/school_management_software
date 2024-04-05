import sqlite3

school = sqlite3.connect("school.db")

curs = school.cursor()

curs.execute("""CREATE TABLE teachers (
        teach_id integer,
        teach_name text,
        subject text,
        class_teacher_of integer
    )""")
print(curs.fetchall())
school.commit()
school.close()