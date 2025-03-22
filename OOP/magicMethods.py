# self.__class__ -> refers to the class
# self.__dict__ -> dictionary containing the class's namespace
# self.__doc__ -> class documentation string or none if undefined
# self.__name__ -> class name
# self.__module__ -> module name in which the class is defined
# self.__str__ -> Gives a Human Readable Representation of the Object
# self.__len__ -> Returns the length of the object, Called by the len() function


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = ["Python", "C++", "Java"]

    def __str__(self):
        return f" Your Name is {self.name}, and your Age is {self.age}"
    
    def __len__(self):
        return len(self.skills)

# __str__ is called when you print an object
print(Person("Ahmed", 25)) # Your Name is Ahmed, and your Age is 25

# __len__ is called when you use the len() function on an object

Person1 = Person("Ahmed", 25)
print(f"Length of Skills is {len(Person1)}") # 3
Person1.skills.append("JavaScript")
Person1.skills.append("PHP")
print(f"Length of Skills is {len(Person1)}") #5

