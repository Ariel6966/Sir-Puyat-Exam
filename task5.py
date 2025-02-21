class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"{self.name} received a raise of ₱{amount:.2f}. New salary: ₱{self.salary:.2f}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ₱{self.salary:.2f}")

# Creating an employee object
employee = Employee("Ariel C. Lacambra", "I.T. Support", 75000.00)

# Giving a raise and displaying details
employee.give_raise(5000.00)
employee.display_employee()
