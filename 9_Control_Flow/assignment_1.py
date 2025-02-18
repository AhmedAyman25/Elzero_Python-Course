num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())
operation = input("Enter the operation: ").strip()

if operation == "+":
    print(num1 + num2)
elif operation =="-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "%":
    print(num1 % num2)
else:
    print("Invalid operation")
