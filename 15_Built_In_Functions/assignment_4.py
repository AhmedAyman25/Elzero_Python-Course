def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False
print(my_all([])) # True

print('='*50)

def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

print('='*50)

def my_min(iterable: list | tuple):
    min = iterable[0]
    for element in iterable:
        if element < min:
            min = element
    return min

print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

print('='*50)

def my_max(iterable: list | tuple):
    max = iterable[0]
    for element in iterable:
        if element > max:
            max = element
    return max

print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700