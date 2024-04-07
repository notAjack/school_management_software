#classes class_teacher Fees marks attendance
import sqlite3

#admn_no = input("Enter Admission Number of student: ")
#admn_no.lower

school = sqlite3.connect("school.db")
curs = school.cursor()

print(curs.execute("SELECT admn_no FROM students ORDER BY admn_no DESC LIMIT 1"))


school.commit()
school.close()