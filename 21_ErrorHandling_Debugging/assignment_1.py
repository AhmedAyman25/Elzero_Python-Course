
NUM = input("Add Your Number ")

if len(NUM) > 1:
    raise IndexError("Only One Character Allowed") 
elif not NUM.isdigit():
   raise Exception("Only Numbers Allowed")
elif NUM == '0':
    raise ValueError("Number Must Be Larger Than 0")
else:
    print("####################")
    print(f"The Number Is {NUM}")
    print("####################")
