Skills ={
    "HTML": 90,
    "CSS": 80,
    "Python": 30,
    }
# Add AI to Skills
Skills.update({"AI": 20})
Keys = list(Skills.keys())
Values = list(Skills.values())

print(f"{Keys[0]} Progress Is {Values[0]}%")
print(f"{Keys[1]} Progress Is {Values[1]}%")
print(f"{Keys[2]} Progress Is {Values[2]}%")
print(f"{Keys[3]} Progress Is {Values[3]}%")
