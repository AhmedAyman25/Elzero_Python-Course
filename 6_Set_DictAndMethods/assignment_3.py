my_set = {1,2,3}
print(my_set)
my_set.clear()
print(my_set) # set()
my_set.update(["A","B"])
print(my_set) # {'A', 'B'}
my_set.discard("C")