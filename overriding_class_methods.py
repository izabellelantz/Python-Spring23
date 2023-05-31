"""
Program: overriding_class_methods.py
Name: Izabelle Lantz
Date: 04/05/2023
This program creates a base class Employee and two child classes (Salary or Hourly Employee) and
implements them both.
"""

class Employee:
    """ Employee Class """
    # Constructor
    def __init__(self, lname, fname, addy, phone_num):
        self._last_name = lname
        self._first_name = fname
        self._address = addy
        self._phone_number = phone_num

    def display(self):
        return str(self._first_name) + str(self._last_name) + '\n' + str(self._address) + '\n' + str(self._phone_number)


class SalariedEmployee(Employee):
    """Salaried Employee class deriving from Employee base class"""
    def __init__(self, lname, fname, addy, phone_num, start_day, salary_amt):
        super().__init__(lname, fname, addy, phone_num)
        try:
            salary_amt = int(salary_amt)
        except ValueError:
            raise ValueError
        self._start_date = start_day
        self._salary = salary_amt
        
    def give_raise(self, new_salary):
        self._salary = new_salary
        
    def display(self):
        return str(self._first_name) + ' ' + str(self._last_name) + '\n' + str(self._address) + '\n' \
            + str(self._phone_number) + ' Start Date:' + str(self._start_date) + '\n' + 'Salary: $' + str(self._salary)


salary_emp = SalariedEmployee('Lantz', 'Izabelle', '999 Clear Road, Des Moines, IA', '(515)999-0000', '04/05/2023', 40000)
print(salary_emp.display())
salary_emp.give_raise(45000)
print(salary_emp.display())

del salary_emp


class HourlyEmployee(Employee):
    """Hourly Employee class deriving from base class Employee"""
    def __init__(self, lname, fname, addy, phone_num, start_day, hourly_pay):
        super().__init__(lname, fname, addy, phone_num)
        try:
            hourly_pay = int(hourly_pay)
        except ValueError:
            raise ValueError
        self._start_date = start_day
        self._wage = hourly_pay
        
    def give_raise(self, new_wage):
        self._wage = new_wage
        
    def display(self):
        return str(self._first_name) + ' ' + str(self._last_name) + '\n' + str(self._address) + '\n' \
            + str(self._phone_number) + ' Start Date: ' + str(self._start_date) + ' Hourly Wage: $' \
                + str(round(self._wage, 2))


hourly_emp = HourlyEmployee('Lantz', 'Izabelle', '999 Clear Rd, Des Moines, IA', '(515)555-5555', '04/05/2023', 10.00)
print(hourly_emp.display())
hourly_emp.give_raise(12.00)
print(hourly_emp.display())

del hourly_emp