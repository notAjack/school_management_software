import sqlite3

#admn_no = input("Enter Admission Number of student: ")
#admn_no.lower
#print(admn_no)
clas = input("Enter Student's current class: ")
clas = clas.lower()
if clas == "lkg":
    clas = 1
elif clas == "ukg":
    clas = 2
else:
    clas = int(clas)
    clas = clas + 2
#print(clas)

oper = input("""
Which Operation Would you like to do?
Update class Teacher [Type teacher]
Update Attendance    [Type attendance]
Update Marks         [Type marks]
Update fees          [Type fees]

=> """)
oper = oper.lower()
#print(oper)

school = sqlite3.connect("school.db")
curs = school.cursor()

#curs.execute("SELECT rowid FROM students")

#if oper == "teacher":


#elif oper == "attendance":

#elif oper == "marks":

#elif oper == "fees":





school.commit()
school.close()