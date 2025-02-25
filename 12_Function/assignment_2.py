def addition(*nums):
    sum = 0
    for num in nums:
        if num == 10:
            continue
        elif num == 5:
            sum -= num
        else:
            sum += num
    return sum

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160