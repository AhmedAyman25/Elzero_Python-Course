# pylint library is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. 
# It can also look for certain type errors.
#  It can be installed using pip by running the command:  pip install pylint

def sayHi(name):
    msg = "Hi"
    return f" {msg} {name}"

sayHi("Ahmed")
# to call the pylint library in the terminal, you can use the following command:
# py -m pylint PATH_TO_YOUR_FILE.py
# to run current file: (py -m pylint h:\Learn_Python\Pylint.py)
