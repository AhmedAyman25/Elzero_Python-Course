# property decorator is a way to use a function as a property
# if a function takes only `self` as a parameter we can use it as a property

class Person:
    def __init__(self, name):
        self.name = name
    @property
    def say_hello(self):
        return f"Hello {self.name}"


p = Person("Ahmed")
print(p.say_hello)  # say_hello is a property not a method, so we can call it without parentheses
