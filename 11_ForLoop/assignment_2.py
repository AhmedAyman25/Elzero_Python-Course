for num in range(1,21):
    if num < 10:
        if num == 6 or num == 8:
            continue
        print(str(num).zfill(2))
    else:
        if num == 12:
            continue
        print(num)
print("All Numbers Printed")        