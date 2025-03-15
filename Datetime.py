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
print('*'*30)

########################## Date Formatting ##########################
# https://strftime.org/
# strftime -> String Format Time
# %Y -> Year
# %m -> Month
# %d -> Day

print(dir(datetime.datetime))
print('*'*30)

# Format Date
Birthday = datetime.datetime(2000,12,16)
print(Birthday.strftime("%Y/%m/%d")) # 2000/12/16
print(Birthday.strftime("%a")) # Sat
print(Birthday.strftime("%A")) # Saturday
print(Birthday.strftime("%m")) # 12
print(Birthday.strftime("%b")) # Dec
print(Birthday.strftime("%B")) # December
print(Birthday.strftime("%y")) # 00
print(Birthday.strftime("%Y")) # 2000

print(Birthday.strftime("%d %B %Y")) # 16 December 2000
print(Birthday.strftime("%d-%b-%Y")) # 16-Dec-2000
print(Birthday.strftime("%d-%m-%Y")) # 16-12-2000

print("*"*30)
def get_n_days_after_date(dateFormat = "%d %m %Y", add_dayes = 120):

    date_n_days_after = datetime.datetime.now() + datetime.timedelta(days = add_dayes)
    return date_n_days_after.strftime(dateFormat)

print(get_n_days_after_date(add_dayes= 100))

# to find the amount of time between dates or determine what the date will be tomorrow. This can be accomplished using timedelta objects

today = datetime.date.today()
print('Today:', today)
yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)

# Fuzzy datetime parsing (extracting datetime out of a text)
# it is possible to extract a date out of a text using the dateutil parser in a "fuzzy" mode
from dateutil.parser import parse
dateTime = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)
print(dateTime)

# Iterate Over Dates
day_delta = datetime.timedelta(days=1)
start_date = datetime.datetime.now()
end_date = start_date + 7 * day_delta

for date in range((end_date - start_date).days):
    print(start_date + date * day_delta)
