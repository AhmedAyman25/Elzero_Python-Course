# Module -> is a file containing Python definitions and statements (Set of functions). 
# The file name is the module name with the suffix .py appended.

# import random module
import random
print(f"Random Float number: {random.random()}")

# show all functions in random module
print(dir(random))

# import one or more functions from random module
from random import randint, choice
print(f"Random Integer number: {randint(1,10)}")
