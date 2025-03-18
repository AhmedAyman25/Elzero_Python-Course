# install pylint if not installed
# write in terminal -> pip install pylint
"""
        This is my Own Module
        This Module Contains One Function
        This Function is Used To Say Hello To Anyone

"""

myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    """"
    This Function Takes List of Names and Print Hello Before Each Name
    Parameter: SomePeoples => List of Names
    """
    for some_one in some_peoples:
        print(f"Hello {some_one}")

say_hello(myFriends)
