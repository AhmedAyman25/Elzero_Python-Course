# datetime is a module
import datetime
print(dir(datetime))
print(dir(datetime.datetime))

# Current date and time
print(datetime.datetime.now())

print('*'*30)

# Current date
print(datetime.datetime.date(datetime.datetime.now()))
print(datetime.datetime.now().date())

print('*'*30)

# Current time
print(datetime.datetime.time(datetime.datetime.now()))
print(datetime.datetime.now().time())

print('*'*30)

# Current Hour
print(datetime.datetime.now().hour)

print('*'*30)

# Current Minute
print(datetime.datetime.now().minute)

print('*'*30)


# Current Second
print(datetime.datetime.now().second)


print('*'*30)
# Current Year
print(datetime.datetime.now().year)

print('*'*30)

# Current month
print(datetime.datetime.now().month)

print('*'*30)

# Current Day
print(datetime.datetime.now().day)

print('*'*30)

# Strat and End of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print('*'*30)

# Strat and End of Time
print(datetime.time.min)
print(datetime.time.max)

print('*'*30)

# Print Specific Date
print(datetime.datetime(2021, 6, 1))
print(datetime.datetime(2021, 6, 1,10,30,45,25541))

print('*'*30)

# Subtract Dates
MyBirthday = datetime.datetime(2000,12,16)
CurrentDate = datetime.datetime.now()
print(f"I Lived For : {CurrentDate - MyBirthday}")
print(f"I Lived For : {(CurrentDate - MyBirthday).days} Days")



