import sqlite3

studentorteacher = input("Enter Student Or Teacher: ")
studentorteacher.lower

school = sqlite3.connect("school.db")
curs = school.cursor()

if studentorteacher == "teacher":
    print(curs.execute("""SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()
    """))

elif studentorteacher == "student":    
    print(curs.execute("""SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()
    """))
sqlite.listdb()
school.commit()
school.close()

#INSERT INTO teachers VALUES(