import sqlite3

studentorteacher = input("Enter Student Or Teacher: ")
studentorteacher.lower
student_columns = ("name", "parents_name", "address", "in_school", "current_class", "join_class_year", "entrance_score", "from_kg" )
teacher_columns = ("name", "subject", "class_teacher_of")
school = sqlite3.connect("school.db")
curs = school.cursor()

if studentorteacher == "teacher":
    for i in teacher_columns:
        for j in len(teacher_columns):
            student_columns[j] = input("Enter "+ i + ": ")
            print(j)
        
print(teacher_columns)

#elsif studentorteacher == "student":
#    print("haha")

school.commit()
school.close()

#INSERT INTO teachers VALUES(