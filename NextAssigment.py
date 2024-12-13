import random

class Employee:
    def __init__(self, name, department, job_title):
        self.name = name
        self.id_number = random.randint(10000, 99999)
        self.department = department
        self.job_title = job_title
    def display_info(self):
        return f"Name: {self.name}, ID Number: {self.id_number}, Department: {self.department}, Job Title: {self.job_title}"
def main():
    employees = []
    again = True
    empl = True
    i = 1
    while again:
        try:
            choice = int(input("Menu\n----\n1. Search for employee\n2. Add new employee\n3. Edit employee data\n4. Delete employee data\n5. Quit\n\n: "))
            if choice == 1:
                pass
            elif choice == 2:
                print(f"\nEnter details for Employee {i}:")
                name = input("Enter employee name: ")
                department = input("Enter employee department: ")
                job_title = input("Enter employee job title: ")
                a = input("Do you want to enter another employee's information? (yes/no): ")

                employee = Employee(name, department, job_title)
                employees.append(employee)
                i+=1
                if a.lower() == "no" or a.lower() == "n":
                    again = False


            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                break
        except ValueError as e:
            print(f"{e}\n\nChoice must be a numerical value.\n")

    print("\nEmployee Information:")
    for employee in employees:
        print(employee.display_info())
    save_to_file = input("\nDo you want to save employee data to a file? (yes/no): ")
    if save_to_file.lower() == "yes" or save_to_file.lower() == "y":
        with open("EmployeeInfo.txt", "w") as file:
            for employee in employees:
                file.write(employee.display_info() + "\n")
        print("Employee data saved to EmployeeInfo.txt")

main()