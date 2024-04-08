import sqlite3

admn_no = input("Enter Admission Number of student: ")
admn_no.lower
print(admn_no)


school = sqlite3.connect("school.db")
curs = school.cursor()

for i in range(1,15):
    curs.execute(f"INSERT INTO {admn_no} (classes) VALUES ({i})")

school.commit()
school.close()