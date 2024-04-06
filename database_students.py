import sqlite3

school = sqlite3.connect("school.db")

curs = school.cursor()

curs.execute("""CREATE TABLE students (
        admn_no integer PRIMARY KEY AUTOINCREMENT,
        student_name text,
        parents_name text,
        address text,
        in_school text,
        current_class text,
        join_class_year text,
        entrance_score text,
        from_kg text
    )""")
print(curs.fetchall())
school.commit()
school.close()