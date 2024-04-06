import sqlite3

studentorteacher = input("Enter Student Or Teacher: ")
studentorteacher.lower
student_columns = ["name", "parents_name", "address", "in_school", "current_class", "join_class_year", "entrance_score", "from_kg" ]
student_columns_values = []
teacher_columns = ["name", "subject", "class_teacher_of"]
teacher_columns_values = []
school = sqlite3.connect("school.db")
curs = school.cursor()

if studentorteacher == "teacher":
    for i in range(len(teacher_columns)):
        j=0
        teacher_columns_values.append(input("Enter "+ teacher_columns[i] + ": "))
        print(teacher_columns_values[j])
        j+=1
        i+=1        
print(teacher_columns)

#elsif studentorteacher == "student":
#    print("haha")

school.commit()
school.close()

#INSERT INTO teachers VALUES(