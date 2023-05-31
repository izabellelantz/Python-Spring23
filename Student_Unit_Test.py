"""
Program: student_unit_test.py
Name: Izabelle Lantz
Date: 03/29/2023
This program tests the class student using unit tests
"""
import unittest
from Student import Student as St

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = St('Lantz', 'Izabelle', 'CIS', 4.0)
    
    def tearDown(self):
        del self.student
        
    def test_object_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Lantz')
        self.assertEqual(self.student.first_name, 'Izabelle')
        self.assertEqual(self.student.major, 'CIS')
        self.assertEqual(self.student.gpa, '4.0')
        
    def test_object_created_all_attributes(self):
        student = St('Lantz', 'Izabelle', 'CIS', 4.0)
        assert student.last_name == 'Lantz'
        assert student.first_name == 'Izabelle'
        assert student.major == 'CIS'
        assert student.gpa == 4.0
        
    def test_student_str(self):
        self.assertEqual(str(self.student), 'Lantz, Izabelle:')
        
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = St('33', 'Belle', 'CIS', 4.0)
            
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = St('Lantz', '34355', 'CIS', 4.0)
            
    def test_object_not_created_gpa(self):
        with self.assertRaises(ValueError):
            s = St('Lantz', 'Belle', 'CIS', 444)


if __name__ == '__main__':
    unittest.main()