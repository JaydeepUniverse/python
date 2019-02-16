#!/usr/bin/env python2.7
class Animal():
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        print name

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print name

class Person():
    def __init__(self, name):
        self.name = name
        self.pet = None
        print name

class Employee(Person):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print name
        print salary

class Fish():
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

Dog("rover")
Cat("cutie")
Person("mary")
Employee("frank", 120000)
flipper = Fish()
crouse = Salmon()
harry = Halibut()
