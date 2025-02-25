def get_people_scores(name = '', **scores):
    if len(name) > 0 and len(scores) > 0:
        print(f"Hello {name} This Is Your Score Table:")
        for key,value in scores.items():
            print(f"{key} => {value}")
    elif len(name) > 0 and len(scores) == 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        for key,value in scores.items():
            print(f"{key} => {value}")



# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"
print('*'*40)
# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"
print('*'*40)
# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"
print('*'*40)
# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"
