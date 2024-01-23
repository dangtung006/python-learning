class Employee:
    co_salary = 1.04
    # __co_salary = 1.04 private proverty , can not access outsite class
    # _co_salary = 1.04 protected proverty, access from child class

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
    
    def getFullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay
    
    def __repr__(self):
        return f"Employee: {self.firstname} {self.lastname}, payment : {self.pay} "

class Developer(Employee):
    co_salary = 1.01
    def __init__(self, firstname, lastname, pay, program_ln):
        super.__init__(firstname, lastname, pay)
        self.program_ln = program_ln

class Manager(Employee):
    co_salary = 1.5
    def __init__(self, firstname, lastname, pay, employees = None ):
        super.__init__(firstname, lastname, pay)

        if employees == None:
            self.employees = []
        else :
            self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees :
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

