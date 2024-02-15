import unittest
from employee_management_system import EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.ems = EmployeeManagementSystem()
        self.ems.create_employee("John Doe", 30, 1, "HR")
        self.ems.create_employee("Jane Smith", 25, 2, "Engineering")

    def test_create_employee(self):
        self.ems.create_employee("Alice", 35, 3, "Marketing")
        self.assertEqual(len(self.ems.employees), 3)

    def test_retrieve_employee_by_id(self):
        employee = self.ems.retrieve_employee_by_id(1)
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.age, 30)
        self.assertEqual(employee.department, "HR")

    def test_delete_employee_by_id(self):
        self.ems.delete_employee_by_id(1)
        self.assertEqual(len(self.ems.employees), 1)
        self.assertIsNone(self.ems.retrieve_employee_by_id(1))

if __name__ == '__main__':
    unittest.main()

