my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output
unique_list = set(my_list)
print(unique_list) # 1, 2, 3, 4, 5 
unique_list = list(unique_list)
print(type(unique_list))# <class 'list'>
print(unique_list[:len(unique_list)-1]) # 1, 2, 3, 4

