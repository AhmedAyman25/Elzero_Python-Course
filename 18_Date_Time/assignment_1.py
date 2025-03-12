import datetime

oldDate = datetime.datetime(2021,6,25).date()
currentDate = datetime.datetime.now().date()

print(f"Days From {oldDate} To {currentDate} Is => {(currentDate - oldDate).days}")