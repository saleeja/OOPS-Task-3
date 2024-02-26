"""Create a class Employee with name and salary attributes.
The salary must be calculated and should be initialized to zero.
Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You 
can give no of hours to the method as an argument.
Now create a child class PartTimeEmployee by inheriting the Employee class, and by using method 
overriding (create salary calculation method in this class also with the same name)
get the salary of part time employee by multiplying no of hours worked by 150.
Create 3 objects for each class.
Now implement '+' operator overloading and find the total salary expense for keeping those 
employees by adding up the objects together.
Eg:
e1 = Employee(name="John")
e1.update_salary(hours=6)
e2 = Employee(name="Robin")
e2.update_salary(hours=8)
e3 = PartTimeEmployee(name="Jake")
e3.update_salary(hours=8)
# The below line should work.
total_expense = e1 + e2 + e3"""



class Employee:
    
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def calculate_salary(self, hours):
        # Standard rate of $200 per hour for a full-time employee
        self.salary = hours * 200
    # Overloaded addition operator to combine total expenses of two employees
    def __add__(self, other):
        total_expense = Employee(f"Total Expense for {self.name} and {other.name}")
        total_expense.salary = self.salary + other.salary
        return total_expense

    def __str__(self): # String representation of an employee, including their name and salary
        return f"{self.name}'s salary: ${self.salary}" if self.salary else f"{self.name} (No salary entered)"

class PartTimeEmployee(Employee):
    def calculate_salary(self, hours):
        # For part-time employees, assuming a rate of $150 per hour
        self.salary = hours * 150

    def __add__(self, other): # Overloaded addition operator for part-time employees
        total_expense = PartTimeEmployee(f"Total Expense for {self.name} and {other.name}")
        total_expense.salary = self.salary + other.salary
        return total_expense

    def __str__(self):  #String representation of a part-time employee, including their name and salary
        return f"{self.name}'s salary: ${self.salary}" if self.salary else f"{self.name} (No salary entered)"
# Calculate the total expense by adding up the salaries of all employees
def calculate_total_expense(employees):
    if not employees:
        return Employee("No employees") 
    
    total_expense = employees[0]
    for employee in employees[1:]:
        total_expense = total_expense + employee
    return total_expense

full_time_employees = []
part_time_employees = []

while True:
    employee_type = input("""Choose an option:\n1. Add full-time employee \n2. Add part-time employee \n3. Calculate total expense \n4. Quit \nEnter the option: """)

    if employee_type == '4':
        break  # Exit the loop if the user enters 'Q'
        
        # Create a full-time employee object and calculate salary
    if employee_type in ('1', '2'):
        name = input("Enter name: ")
        hours = int(input("Enter hours worked: "))
     # Create a part-time employee object and calculate salary
    if employee_type == '1':
        employee = Employee(name=name)
        employee.calculate_salary(hours=hours)
        full_time_employees.append(employee)
    elif employee_type == '2':
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
            print(f"\nTotal Salary Expense: ${total_expense.salary}")
            break
        else:
            print("\n Please enter employees.")
    else:
        print("Invalid input.")

# output
"""
Choose an option:
1. Add full-time employee  
2. Add part-time employee  
3. Calculate total expense 
4. Quit
Enter the option: 1
Enter name: sale
Enter hours worked: 6
Choose an option:
1. Add full-time employee
2. Add part-time employee
3. Calculate total expense
4. Quit
Enter the option: 2
Enter name: dne
Enter hours worked: 4
Choose an option:
1. Add full-time employee
2. Add part-time employee
3. Calculate total expense
4. Quit
Enter the option: 3

Details of Entered Employees:
sale's salary: $1200
dne's salary: $600

Total Salary Expense: $1800"""