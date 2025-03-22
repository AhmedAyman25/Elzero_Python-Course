# Class is the Blueprint or template for creating objects
# It defines attributes(data) and mathods(behaviors) that the objects of that class will have
# Classes provide a means of bundling data and functionality together
# Class instantiate Means create an instance (object) of a class
# Object is an instance of a class
# Class defined by the keyword `class`
# Class name should be in PascalCase (Capitalize the first letter of each word)
# when creating object from class, the constructor is called automatically
# The constructor is a special method that is called when an object is created from a class
# The constructor is defined using the `__init__` method
# The `__init__` method is called automatically when an object is created from a class
# The `__init__` method is used to initialize the attributes of the object
# self is a reference (point) to the current instance of the class
# self is used to access variables that belong to the class
# self must be the first parameter of any method in the class

# instance attributes -> attributes defined in the constructor 
# instance methods -> Take self as the first parameter which refers to the current object
# instance methods can access the attributes and methods of the same class

# class attributes -> attributes defined outside the constructor
# class methods -> Take cls as the first parameter which refers to the class
# class methods marked with @classmethod decorator
# don't need to create an object to access class attributes and methods


class Car:
    # class attributes
    not_allowed_colors = ["Brown", "Rose", "Yellow"]
    car_count = 0

    # Constructor
    def __init__(self,CarName, CarColor, CarModel):
        # instance attributes
        self.name = CarName
        self.color = CarColor
        self.model = CarModel
        Car.car_count += 1 # the same as self.__class__.car_count += 1

    # instance method
    def get_car_info(self):
        if self.color in Car.not_allowed_colors:
            raise ValueError("Color is not allowed")
        else:
            return f"Car Name: {self.name} Car Color: {self.color} Car Model: {self.model}"
    
    # class method
    @classmethod
    def get_car_count(cls):
        return f"Car Count: {cls.car_count}"

# Create instances        
bmw = Car("BMW","Red","2020")
kia = Car("KIA","Black","2021")
mg = Car("MG","White","2022")


# mercedes = Car("Mercedes","Brown","2023")
# print(mercedes.get_car_info())

# print(bmw.name,bmw.color,bmw.model)
# print(kia.name,kia.color,kia.model)
# print(mg.name,mg.color,mg.model)
# print(kia.__class__)
print(Car.get_car_count())
print(Car.car_count)