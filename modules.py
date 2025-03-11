# Module -> is a file containing Python definitions and statements (Set of functions). 
# The file name is the module name with the suffix .py appended.

# package -> is a directory which contains a module or a collection of modules.
# package is a namespace that contains multiple packages and modules themselves.
# external package -> is a package that is not part of the Python standard library.
# internal package -> is a package that is part of the Python standard library.
# download external package with Python Package Manager  -> pip install package_name
# download external package with Python Package Manager and specify version -> pip install package_name==version
# download external package with Python Package Manager and specify version range -> pip install package_name>=version
# upgrade external package with Python Package Manager  -> pip install --upgrade package_name
# uninstall external package with Python Package Manager  -> pip uninstall package_name
# show all installed packages -> pip list
# show all installed packages with version -> pip freeze

#Packages and Module Directory "https://pypi.org/"

# import random module
import random
print(f"Random Float number: {random.random()}")

# show all functions in random module
print(dir(random))

# import one or more functions from random module
from random import randint, choice
print(f"Random Integer number: {randint(1,10)}")

# import sys module
import sys
print(sys.path) # show all paths that python interpreter will search for modules
# add new path to sys.path
sys.path.append('C:\\Users\\Ahmed\\Desktop\\Python\\Python-Bootcamp\\modules') 
print(sys.path)

# import myOwnModule module
import myOwnModule
myOwnModule.sayHello("Ahmed")
myOwnModule.sayBye("Omar")
myOwnModule.sayWelcome("Ali")
myOwnModule.sayGoodBye("Sayed")

# import myOwnModule module and rename it (Alias)
import myOwnModule as myModule
myModule.sayHello("Ahmed")
myModule.sayBye("Omar")
myModule.sayWelcome("Ali")
myModule.sayGoodBye("Sayed")

# install termcolor package
# pip install termcolor

# install figlet package
# pip install pyfiglet
import termcolor, pyfiglet
print(termcolor.colored("Hello World", color="red"))
print(pyfiglet.figlet_format("Hello World"))
