def get_score(**grades):
    for key,value in grades.items():
        print(f"{key} => {value}")






# Tests
get_score(Math=90, Science=80, Language=70)

# Output
"Math => 90"
"Science => 80"
"Language => 70"

# Tests
get_score(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"