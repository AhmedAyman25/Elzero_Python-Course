students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
A,B,C,D = 100,80,40,20
#Method 1
for student in students:
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    total_points = 0
    for point in students[student]:
        if students[student][point] == 'A':
            print(f"-{point} => {A} Points")
            total_points += A
        elif students[student][point] == 'B':
            print(f"-{point} => {B} Points")
            total_points += B
        elif students[student][point] == 'C':
            print(f"-{point} => {C} Points")
            total_points += C
        elif students[student][point] == 'D':
            print(f"-{point} => {D} Points")
            total_points += D
    print(f"Total Points For {student} Is {total_points}")

print("="*30)      

# Method 2 using items()
for std_key, std_value in students.items():
    print("------------------------------")
    print(f"-- Student Name => {std_key}")
    print("------------------------------")
    total_points = 0
    for point_key, point_value in std_value.items():
        if point_value == 'A':
            print(f"-{point_key} => {A} Points")
            total_points += A
        elif point_value == 'B':
            print(f"-{point_key} => {B} Points")
            total_points += B
        elif point_value == 'C':
            print(f"-{point_key} => {C} Points")
            total_points += C
        elif point_value == 'D':
            print(f"-{point_key} => {D} Points")
            total_points += D
    print(f"Total Points For {std_key} Is {total_points}")


