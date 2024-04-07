#classes class_teacher Fees marks attendance
import sqlite3

admn_no = input("Enter Admission Number of student: ")
admn_no.lower

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