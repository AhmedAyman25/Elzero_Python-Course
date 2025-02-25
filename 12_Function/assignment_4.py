def say_hello(name = 'Unknown' , age = 'Unknown', country = 'Unknown'):
    return (f"Hello {name} Your Age Is {age} And You Live In {country}")




# Input
print(say_hello("Osama", 38, "Egypt"))

# Output
"Hello Osama Your Age Is 38 And You Live In Egypt"

# Input
print(say_hello())

# Output
"Hello Unknown Your Age Is Unknown And You Live In Unknown"