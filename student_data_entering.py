import sqlite3

admn_no = input("Enter Admission Number of student: ")
admn_no.lower
#print(admn_no)


school = sqlite3.connect("school.db")
curs = school.cursor()

curs.execute("SELECT rowid FROM students")

school.commit()
school.close()