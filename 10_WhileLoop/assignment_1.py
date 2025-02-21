num = int(input("Please Enter a Number: "))

if num == 0:
    print("Number 0 Is Not Larger Than 0")
else:    
    counter = 0
    while num > 0:
        if num - 1 == 0:
            break
        if num - 1 == 6:
            num -= 1
            continue
        print (f"{num - 1}")
        counter +=1
        num -= 1

    print(f"{counter} Numbers Printed Successfully.")