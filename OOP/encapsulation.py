# Encapsulation -> hiding of data and methods from the outside world
# Encapsulation is achieved by making the attributes private

# types of encapsulation -> public, private, protected

# public -> accessible from anywhere

# private -> accessible only from within the class
    # private attributes and methods are prefixed with a Two underscores __
    # private attributes and methods are not accessible from outside the class

# protected -> accessible from within the class and its subclasses
     # protected attributes and methods are prefixed with a single underscore _
    
######################## Protected ########################

class Member:
    def __init__(self, name):
        self._name = name # protected attribute
        
m1 = Member("Ahmed")
print(m1._name) # protected attribute can be accessed from outside the class

######################## Private ########################

class Person:
    def __init__(self, name):
        self.__name = name # private attribute

p = Person("Mohammed")
print(p._Person__name) # in this case private attribute can be accessed from outside the class
#print(p.__name) # (Error) -> private attribute cannot be accessed from outside the class