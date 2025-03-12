import datetime

todayDate = datetime.datetime.now().date()

print(todayDate.strftime("%Y-%m-%d"))
print(todayDate.strftime("%b %d, %Y"))
print(todayDate.strftime("%d - %b - %Y"))
print(todayDate.strftime("%d / %b / %y"))
print(todayDate.strftime("%d / %B / %Y"))
print(todayDate.strftime("%a, %d %B %Y"))