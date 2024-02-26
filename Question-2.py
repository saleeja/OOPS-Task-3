"""Extend the above solution and find the average expense per employee.
The calculation must be dynamic, there should be no need for you to manually code each addition 
operations. This can be done by keeping track of the objects being created – in a list (But don’t
manually append the objects to a list, this must happen when the objects are being created)"""


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def calculate_salary(self, hours):
        # standard rate of $200 per hour for a full-time employee
        self.salary = hours * 200

    def __add__(self, other):
        # Overloaded addition operator to combine total expenses of two employees
        total_expense = Employee(f"Total Expense for {self.name} and {other.name}")
        total_expense.salary = self.salary + other.salary
        return total_expense

    def __str__(self):
        # String representation of an employee, including their name and salary
        return f"{self.name}'s salary: ${self.salary}" if self.salary else f"{self.name} (No salary entered)"

class PartTimeEmployee(Employee):
    def calculate_salary(self, hours):
        # For part-time employees, assuming a rate of $150 per hour
        self.salary = hours * 150

    def __add__(self, other):
        # Overloaded addition operator for part-time employees
        total_expense = PartTimeEmployee(f"Total Expense for {self.name} and {other.name}")
        total_expense.salary = self.salary + other.salary
        return total_expense

    def __str__(self):
        # String representation of a part-time employee, including their name and salary
        return f"{self.name}'s salary: ${self.salary}" if self.salary else f"{self.name} (No salary entered)"

def calculate_total_expense(employees):
    # Calculate the total expense by adding up the salaries of all employees
    if not employees:
        return Employee("No employees") 

    total_expense = employees[0]
    for employee in employees[1:]:
        total_expense = total_expense + employee
    return total_expense

full_time_employees = []
part_time_employees = []

while True:
    employee_type = input("""Choose an option:
                          1. Add full-time employee
                          2. Add part-time employee
                          3. Calculate total expense
                          4. Quit: """)

    if employee_type == '4':
        break  # Exit the loop if the user enters '4'

    if employee_type in ('1', '2'):
        name = input("Enter name: ")
        hours = int(input("Enter hours worked: "))

        if employee_type == '1':
            # Create a full-time employee object and calculate salary
            employee = Employee(name=name)
            employee.calculate_salary(hours=hours)
            full_time_employees.append(employee)
        elif employee_type == '2':
            # Create a part-time employee object and calculate salary
            part_time_employee = PartTimeEmployee(name=name)
            part_time_employee.calculate_salary(hours=hours)
            part_time_employees.append(part_time_employee)
    elif employee_type == '3':
        # Print details of all entered employees
        print("\nDetails of Entered Employees:")
        for emp in full_time_employees + part_time_employees:
            print(emp)

        # Calculate total salary expense
        total_expense = calculate_total_expense(full_time_employees + part_time_employees)
        if total_expense.salary:
            average_expense = total_expense.salary / len(full_time_employees + part_time_employees)
            print(f"\nTotal Salary Expense: ${total_expense.salary}")
            print(f"Average Expense per Employee: ${average_expense}")
            break  # Exit the loop after calculating and printing the total and average expense
        else:
            print("\nPlease enter employees.")
    else:
        print("Invalid input.")

