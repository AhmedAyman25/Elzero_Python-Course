values = (0, 1, 2)

if any(values):
 # set 0 to my_var, because values contains at least one True value (1,2)
  my_var = 0 

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
  # display Good, because all elements in all(my_list[:4]) are True
  # display Good, because all elements in all(my_list[:6]) are True
  print("Good")

else:

  print("Bad")

# "Good"