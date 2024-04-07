#classes class_teacher Fees marks attendance
import sqlite3

#admn_no = input("Enter Admission Number of student: ")
#admn_no.lower

school = sqlite3.connect("school.db")
curs = school.cursor()

curs.execute("SELECT admn_no FROM students ORDER BY admn_no DESC LIMIT 1")
admn_no = ("s" + str(curs.fetchone()[0]))
print(admn_no)
curs.execute(f"""CREATE TABLE {admn_no} (
    classes integer PRIMARY KEY AUTOINCREMENT,
    class_teacher text,
    outfees1 text,
    outfees2 text,
    outfees3 text,
    attendance text,
    marks1 text,
    marks2 text,
    marks3 text
)""")


school.commit()
school.close()