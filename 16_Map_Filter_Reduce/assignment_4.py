skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
for counter , skill in enumerate(reversed(skills),50):
    if isinstance(skill, int):
        continue
    print(f"{counter} - {skill}")

   
print('='*30)

counter = 50
for skill in reversed(skills):
    if isinstance(skill, int):
        counter += 1
        continue
    print(f"{counter} - {skill}")
    counter += 1
# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"