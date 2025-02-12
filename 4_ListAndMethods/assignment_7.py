friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

 # Method 1 to merge lists
#friends = friends + employees + school


# Method 2 to merge lists
friends.extend(employees)
friends.extend(school)
print(friends) # ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]