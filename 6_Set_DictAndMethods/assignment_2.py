nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Method 1 
print(nums.union(letters))  # {1, 2, 3, "A", "B", "C"}


# Method 2
nums.update(letters)
print(nums) # {1, 2, 3, "A", "B", "C"}

#Method 3 
print(nums | letters)  # {1, 2, 3, "A", "B", "C"}





