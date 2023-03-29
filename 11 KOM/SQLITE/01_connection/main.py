import sqlite3

connection = sqlite3.connect("employee.db") #conn

cursor = connection.cursor() # c / cur

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    first TEXT,
    last TEXT,
    salary INTEGER
    )
    """)

cursor.execute("INSERT INTO employees VALUES ('steve', 'richardson', 1200000)") # CREATE

# cursor.execute("SELECT * FROM employees")

# emps = cursor.fetchall()
# print(emps)
# for row in emps:
#     print(row)

cursor.execute("SELECT * FROM employees WHERE last='richardson'")

emp = cursor.fetchone()
print(emp)

connection.commit()


connection.close()
