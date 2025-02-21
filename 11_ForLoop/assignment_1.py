# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
Counter = 1
for num in my_nums:
    if num % 5 == 0:
        print(f"{Counter} => {num}")
        Counter += 1
print("All Numbers Printed")

