import sqlite3

studentorteacher = input("Enter Student Or Teacher: ")
studentorteacher.lower
student_columns = ["student_name", "parents_name", "address", "in_school", "current_class", "join_class_year", "entrance_score", "from_kg" ]
teacher_columns = ["teacher_name", "subject", "class_teacher_of"]

school = sqlite3.connect("school.db")
curs = school.cursor()

if studentorteacher == "teacher":
    print("Skip If you don't Know Any of The Details.")
    for i in range(len(teacher_columns)):
        teacher_columns[i] = (input("Enter " + teacher_columns[i] + ": "))
        i+=1        
    curs.execute("INSERT INTO teachers (teacher_name, subject, class_teacher_of) VALUES (?,?,?)", teacher_columns)

elif studentorteacher == "student":
    print("Skip If you don't Know Any of The Details.")
    for i in range(len(student_columns)):
        student_columns[i] = input("Enter " + student_columns[i] + ": ")
        i+=1
    curs.execute("INSERT INTO students (student_name, parents_name, address, in_school, current_class, join_class_year, entrance_score, from_kg) VALUES (?,?,?,?,?,?,?,?)", student_columns)

school.commit()
school.close()