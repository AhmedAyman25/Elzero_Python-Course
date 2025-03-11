from functools import reduce


def multiply(num1, num2):
    return num1 * num2

nums = [2, 4, 6, 2]

result = reduce(multiply, nums)
print(result)