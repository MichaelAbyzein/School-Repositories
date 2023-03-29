from os import system

from settings import Settings
from employee import Employee

class App:
    def __init__(self):
        self.settings = Settings()
        self.settings.CUR.execute("""
            CREATE TABLE IF NOT EXISTS employees (
            first TEXT,
            last TEXT,
            salary INTEGER
            )
        """)

    def get_all_emps(self):
        with self.settings.CONN:
            self.settings.CUR.execute("SELECT * FROM employees ORDER BY first")
        return self.settings.CUR.fetchall()

    def insert_emp(self, emp):
        with self.settings.CONN:
            self.settings.CUR.execute("INSERT INTO employees VALUES (:first, :last, :salary)", {"first":emp.first, "last":emp.last, "salary":emp.salary})
    
    def find_emp(self, first):
        with self.settings.CONN:
            self.settings.CUR.execute("SELECT * FROM employees WHERE first=:first", {"first":first}) # Unique ID
        return self.settings.CUR.fetchone()

    def update_salary(self, emp, new_salary):
        with self.settings.CONN:
            self.settings.CUR.execute("UPDATE employees SET salary=:salary WHERE first=:first", {"salary":new_salary, "first":emp.first})
    
    def remove_emp(self, emp):
        with self.settings.CONN:
            self.settings.CUR.execute("DELETE FROM employees WHERE first=:first AND last=:last", {"first":emp.first, "last":emp.last})

    def mainloop(self):
        while True:
            system("cls")

            print(self.settings.MENU)

            option = input("Option :").lower()
            if option == 'q':
                print("Thanks!")
                break

            elif option == '1':
                system("cls")
                emps = self.get_all_emps()
                print(emps)
                input("Press Enter To Return")

            elif option == '2':
                system("cls")
                first, last, salary = input("Insert (first, last, salary) : ").split()
                emp = Employee(first, last, salary)
                self.insert_emp(emp)
                print("DONE")
                input("Press Enter to Return")

            elif option == '3':
                system("cls")
                first = input("Insert First Name : ")
                res = self.find_emp(first)
                if res:
                    print(res)
                else:
                    print("Nothing!")
                input("Press Enter to Return")

            elif option == '4':
                system("cls")
                first = input("Insert The First Name : ")
                emp = self.find_emp(first)
                if emp:
                    new_salary = int(input("Insert The New Salary : "))
                    emp = Employee(emp[0], emp[1], emp[2])
                    self.update_salary(emp, new_salary)
                    print("DONE")
                else:
                    print("Employee Not Found!")
                input("Press Enter to Return")

            elif option == '5':
                system("cls")
                first = input("Insert The First Name : ")
                emp = self.find_emp(first)
                if emp:
                    emp = Employee(emp[0], emp[1], emp[2])
                    self.remove_emp(emp)
                    print("Employee Has Been Removed!")
                else:
                    print("Employee Not Found!")
                input("Press Enter to Return")
        
        
        
        self.settings.CONN.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()