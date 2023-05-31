"""
Program: employee.py
Name: Izabelle Lantz
Date: 03/29/2023
This program creates an employee class and creates an object of that class in the driver code
"""

class Employee:
    """ Employee Class """
    # Constructor
    def __init__(self, lname, fname, addy, phone_num, salaried, start_day, salary):
        self._last_name = lname
        self._first_name = fname
        self._address = addy
        self._phone_number = phone_num
        self._is_salaried = salaried
        self._start_date = start_day
        self._salary_amt = salary
    
    def display(self):
        if self._is_salaried:
            return str(self._first_name) + ' ' + str(self._last_name) + '\n' + str(self._address) + '\n' + str(self._phone_number) + '\n' + 'Salaried Employee: $' + str(float(self._salary_amt))
        else:
            return str(self._first_name) + str(self._last_name) + '\n' + str(self._address) + '\n' + str(self._phone_number) + '\n' + 'Hourly Employee: $' + str(float(self._salary_amt)) + '/hour'


# Driver
emp = Employee('Ruiz', 'Matthew', '4323 Cedar Ave, Clive', '(515)000-0000', True, 6-8-2019, 40000.00)
print(emp.display()) # display returns a str, so print the information

del emp

emp = Employee('Lantz', 'Izabelle', '000 Bryan St, Waukee', '(000)555-5555', False, 9-9-2022, 12.50)
print(emp.display())

del emp