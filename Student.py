"""
Program: Student.py
Name: Izabelle Lantz
Date: 03/29/2023
This program creates a class student and validates input and creates an object of the class
"""

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_char = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        if not (name_char.issuperset(lname) and name_char.issuperset(fname)):
            raise ValueError
        if 0.0 > gpa <= 4.0:
            try:
                gpa = float(gpa)
            except ValueError:
                raise ValueError
            
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa
        
    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


student_a = Student('Lantz', 'Izabelle', 'CIS', 4.0)
print(student_a.__str__())

del student_a

student_b = Student('Mcgee', 'Sarah', 'Business', 3.3)
print(student_b.__str__())
