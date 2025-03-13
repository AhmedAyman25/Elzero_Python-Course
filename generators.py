#--- Generator Functions ---
# A generator function is a special type of function that returns an iterator object.
# This function can be paused and resumed during its execution.
# The yield keyword is used to return data from the generator function.
# The generator function can have multiple yield statements.
# by using the next() function, the generator function can be resumed from where it was paused.
# The generator function can be used in a for loop.

'''
----------------- Yield vs Return -------------
- yield is used in generator functions to provide a sequence of values over time.
    When yield is executed, it pauses the function, returns the current value and retains the state of the function.
    This allows the function to continue from the same point when called again, making it ideal for generating large or complex sequences efficiently.

- return, on the other hand, is used to exit a function and return a final value. 
    Once return is executed, the function is terminated immediately, and no state is retained.
    This is suitable for cases where a single result is needed from a function.

'''

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

gen = myGenerator()
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3
print(next(gen)) #4
# print(next(gen)) #StopIteration

print('*'*30)


# by using the next() function, the generator function can be resumed from where it was paused.

def myGenerator2():
    for i in range(5):
        yield i

gen2 = myGenerator2()
print(next(gen2)) #0
print("I Love Python")
print(next(gen2)) #1
print("I Love Python")
print(next(gen2)) #2
print("I Love Python")
print(next(gen2)) #3
print("I Love Python")
print(next(gen2)) #4
