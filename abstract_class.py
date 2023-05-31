"""
Program: abstract_class.py
Name: Izabelle Lantz
Date: 04/12/2023
This program creates an abstract base class (Rider) and two sub classes that override the methods in Rider
"""
from abc import ABC, abstractmethod


class Rider(ABC): 
    @abstractmethod
    def ride(self):
        pass
    
    def rider(self):
        pass


class Bicycle(Rider):
    def __init__(self): 
        self.rides = 'Human powered, not enclosed.'
        self.riders = '1 or 2 if tandem' 
        
    def ride(self):
        return self.rides, self.riders
    
    def __str__(self):
        return str(self.ride())


class Motorcycle(Rider):
    def __init__(self):
        self.rides = 'Engine powered, not enclosed.' 
        self.riders = 'Up to 2'
        
    def ride(self):
        return self.rides, self.riders
    
    def __str__(self):
        return str(self.ride())


class Car(Rider):
    def __init__(self):
        self.rides = 'Engine powered, enclosed.'
        self.riders = '1+ comfortably'
        
    def ride(self):
        return self.rides, self.riders
    
    def __str__(self):
        return str(self.ride())
    

# driver
b = Bicycle()
m = Motorcycle()
c = Car()

print(str(b))
print(str(m))
print(str(c))
