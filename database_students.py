import sqlite3

school = sqlite3.connect("school.db")

curs = school.cursor()

curs.execute("""CREATE TABLE students (
        admn_no integer,
        name text,
        parents_name text,
        address text,
        in_school text,
        current_class integer,
        join_class_year integer,
        entrance_score integer,
        from_kg text
    )""")
print(curs.fetchall())
school.commit()
school.close()