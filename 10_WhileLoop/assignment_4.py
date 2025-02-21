my_friends = []
maxSize = 4

name = input(" Enter the Name: ").strip()
while maxSize > 0:
    if name.isupper():
        print("Invalid Name")
        print(f"Names Left in List Is {maxSize}")
    elif name.islower():
        name = name.capitalize()
        my_friends.append(name)
        print(f"Friend {name} Added => 1st Letter Become Capital")
        maxSize -= 1
        print(f"Names Left in List Is {maxSize}" if maxSize >0 else f" List is Completed")
    elif name == name.capitalize():
        my_friends.append(name)
        print(f"Friend {name} Added")
        maxSize -= 1
        print(f"Names Left in List Is {maxSize}" if maxSize >0 else f" List is Completed")

    if maxSize>0:
        name = input(" Enter the Name: ").strip()