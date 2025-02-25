def calculate(num1, num2, operation = 'add'):
    if operation.lower() == 'add' or operation.lower() == 'a':
        return num1 + num2

    elif operation.lower() == 'subtract' or operation.lower() == 's':
        return num1 - num2

    elif operation.lower() == 'multiply' or operation.lower() == 'm':
        return num1 * num2

    else: 
        print("This Operation Does not Available!")

# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200