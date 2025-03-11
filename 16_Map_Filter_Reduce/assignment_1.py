def remove_chars(item):
    return item[1:-1]
    
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars, friends_map)

for item in cleaned_list:
    print(item)
print("-"*50)
#################### use lambda function ####################
for item in map(lambda item: item[1:-1], friends_map):
    print(item)