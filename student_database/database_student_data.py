import sqlite3

studentorteacher = input("Enter Student Or Teacher")
studentorteacher.lower

school = sqlite3.connect("school.db")
curs = school.cursor()

if studentorteacher == student:
    
    curs.execute("""INSERT INTO students VALUES()
        """)

school.commit()
school.close()