# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif","omar"]
index , counter = 0,0
sizeOfList = len(friends) 
while index < sizeOfList:
    if friends[index][0] == friends[index][0].lower():
        index +=1
        counter +=1
        continue
    else:
        print(friends[index])
        index +=1

print(f"Friends Printed And Ignored Names Count Is {counter}")
