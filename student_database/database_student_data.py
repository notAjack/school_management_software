import sqlite3

studentorteacher = input("Enter Student Or Teacher")

school = sqlite3.connect("school.db")
curs = school.cursor()
curs.execute("""INSERT INTO school VALUES()
    """)
print(curs.fetchall())
school.commit()
school.close()