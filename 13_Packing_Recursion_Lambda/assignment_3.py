scores_list = {
    "Math":"90",
    "Science":"80",
    "Language":"70"
}

def get_the_scores(name='',**scores):
    if len(name) > 0 and len(scores) > 0:
        print(f"Hello {name} This Is Your Score Table:")
        for subject, score in scores.items():
            print(f"{subject} => {score}")
    elif len(name) > 0 and len(scores) == 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
         for subject, score in scores.items():
            print(f"{subject} => {score}")

# Test 1
get_the_scores("Osama", **scores_list)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_the_scores("Osama")

# Output
"Hello Osama You Have No Scores To Show"

# Test 3
get_the_scores(**scores_list)

# Output
"Math => 90"
"Science => 80"
"Language => 70"