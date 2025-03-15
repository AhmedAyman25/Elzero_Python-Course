def sugar_decorator(func):
  def wrapper():
    print("Sugar Added From Decorators")
    func()
    print("####################")
  return wrapper
  
@sugar_decorator
def make_tea():
  print("Tea Created")

@sugar_decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()

