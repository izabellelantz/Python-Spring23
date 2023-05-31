"""
Program: multiple_inheritance.py
Name: Izabelle Lantz
Date: 04/05/2023
This program creates a base class Person and a base class Employee and creates a Manager class
that inherits from both and implements that class.
"""
class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self._last_name = lname
        self._first_name = fname
        self._address = addy
        
    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Employee:
    """Employee class"""
    def __init__(self, lname, fname, start_day, salary_amt):
        try:
            salary_amt = int(salary_amt)
        except ValueError:
            raise ValueError
        self._last_name = lname
        self._first_name = fname
        self._start_date = start_day
        self._salary = salary_amt
        
    def give_raise(self, new_salary):
        self._salary = new_salary
        
    def display(self):
        return str(self._last_name) + ', ' + str(self._first_name) + 'Start Date:' + str(self._start_date) + '\n' \
            + 'Salary: $' + str(self._salary)


class Manager(Person, Employee):
    """ Manager Class deriving from Person and Employee base classes """
    def __init__(self, lname, fname, start_date, salary=40000, dept='', dir_rep = []):
        Person.__init__(self, lname, fname, ', ')
        Employee.__init__(self, lname, fname, start_date, salary)
        self._direct_reports = dir_rep
        self._department = dept
        
    def add_to_report(self, lname, fname, start_date, salary):
        return self._direct_reports.append(lname + ' ' + fname + ' ' + start_date + ' $' + str(salary))
    
    def display_direct_reps(self):
        return self._direct_reports
    
    def display(self):
        return self._last_name + ', ' + self._first_name + ' Start Date:' + str(self._start_date) + '\n' \
            + 'Salary: $' + str(self._salary) + ' Department: ' + self._department


manager1 = Manager('Lantz', 'Izabelle', '04/05/2023', 40000)
print(manager1.display())
manager1.add_to_report('Sarah', 'Tom', '04/04/2020', 10000)
manager1.add_to_report('McGravy', 'Susan', '02/20/2022', 20000)
manager1.add_to_report('Beast', 'Morgan', '03/20/2003', 20000)
print(manager1.display_direct_reps())
manager1.give_raise(42000)
print(manager1.display())

del manager1