# Class Attributes ->  are the variables that are shared across all instances of a class.
#  It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# Instance Attributes -> are the variables that are unique to each instance of a class.
#  They are defined within the constructor method of the class. 
# Each object maintains its own copy of instance variables, independent of other objects.


class Dog:
    # Class Attribute
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age

# Create instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing class and instance attributes
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Max

# Modify instance variables
dog1.name = "Charlie"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)
