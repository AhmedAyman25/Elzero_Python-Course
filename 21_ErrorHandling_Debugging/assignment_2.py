
try:
    LETTER = input("Add Letter From A to Z ")
    if len(LETTER) > 1 or LETTER.isdigit():
        raise IndexError
    elif LETTER != LETTER.upper():
        raise ValueError
except IndexError:
    print("You Must Write One Character Only")
except ValueError:
    print("The Letter Not In A - Z")
else:
    print(f"You Typed {LETTER}")

    


