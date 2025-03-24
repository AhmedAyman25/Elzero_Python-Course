# Abstract Base Class (ABC) -> a class that cannot be instantiated, but can be subclassed
# An abstract base class contains one or more abstract methods
# An abstract method is a method that is declared, but contains no implementation
# An abstract method can only be defined in an abstract base class
# An abstract method can only be overridden by a subclass
# to create an abstract method, we need to import the `abstractmethod` class from the `abc` module,
#  then use the `@abstractmethod` decorator
# To create an abstract base class, we need to import the `ABCMeta` class from the `abc` module
# ABC is a metaclass, which means it is a class that is used to create other classes

from abc import ABCMeta, abstractmethod

class Programming(metaclass = ABCMeta):

    @abstractmethod
    def has_oop(self):
        pass

class Python(Programming):
    def has_oop(self):
        return "Yes"

class Pascal(Programming):
    def has_oop(self):
        return "No"
    
py = Python()
print(py.has_oop())
pas = Pascal()
print(pas.has_oop())