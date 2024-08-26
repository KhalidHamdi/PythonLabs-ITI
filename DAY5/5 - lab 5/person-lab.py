"""
    class Person:
    Private Attributes:
        __name:
        __brith year:

    methods:
        say_hello: prints name whenever called

    properties:
        name
        age
"""

from datetime import date

class Person:
    def __init__(self, name, birthyear):
        self.__name = name
        self.__birthyear = birthyear

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        today = date.today()
        return today.year - self.__birthyear

    def say_hello(self):
        print("Hello " + self.__name)

myperson = Person("Khalid", 2000)
myperson.say_hello()
print(myperson.age)   
print(myperson.name)  
