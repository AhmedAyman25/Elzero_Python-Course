class Food:
    def __init__(self,FoodName, FoodPrice):
        self.name = FoodName
        self.price = FoodPrice
        print("Food Created")

    def eat(self):
        return f"I am eating {self.name}"
    

class Apple(Food):
    def __init__(self,AppleName,ApplePrice):
        # self.name = AppleName
        # self.price = ApplePrice

        # Food.__init__(self,AppleName, ApplePrice) # create instance from base class
        super().__init__(AppleName, ApplePrice) # create instance from base class
        print(f"{self.name} is Created from Apple Class and Price is {self.price}")

    

food = Food("Pizza", 100)

apple = Apple("Apple", 50)

######################## Polymorphism  ########################

# to force the child class to override the parent class method use `raise NotImplementedError`
class A:
    def do_something(self):
        print("I am doing something in A")
        raise NotImplementedError("Subclass must implement this method")

class B(A):
    def do_something(self):
        print("I am doing something in B")

class C(A):
    def do_something(self):
        print("I am doing something in C")


obj = C()
obj.do_something()