class Employee:
    def __init__(self, name, age, employee_id, department):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def create_employee(self, name, age, employee_id, department):
        employee = Employee(name, age, employee_id, department)
        self.employees.append(employee)

    def retrieve_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def delete_employee_by_id(self, employee_id):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == employee_id:
                del self.employees[i]
                return True
        return False

