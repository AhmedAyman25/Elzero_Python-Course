def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Is ")
        for skill in skills:
            print(f"- {skill}")
# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")

# Output
"Hello Osama Your Skills Is"
"- HTML"
"- CSS"
"- JS"
"- Python"

# Input
show_skills("Ahmed")

# Output
"Hello Ahmed You Have No Skills To Show"
