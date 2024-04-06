import sqlite3

studentorteacher = input("Enter Student Or Teacher: ")
studentorteacher.lower
student_columns = ("name", "parents_name", "address", "in_school", "current_class", "join_class_year", "entrance_score", "from_kg" )
teacher_columns = ("name", "subject", "class_teacher_of")
school = sqlite3.connect("school.db")
curs = school.cursor()

if studentorteacher == "teacher":
    for i in teacher_columns:
        i = input("Enter "+ i + ": ")
        print(i)
print(teacher_columns)

elif studentorteacher == "student":

school.commit()
school.close()

#INSERT INTO teachers VALUES(