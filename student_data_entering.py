import sqlite3

#admn_no = input("Enter Admission Number of student: ")
#admn_no.lower
#print(admn_no)
oper = input("""
Which Operation Would you like to do?
Update class Teacher [Type teacher]
Update Attendance    [Type attendance]
Update Marks         [Type marks]
Update fees          [Type fees]

=>
""")
oper.lower
print(oper)
school = sqlite3.connect("school.db")
curs = school.cursor()

#curs.execute("SELECT rowid FROM students")

school.commit()
school.close()