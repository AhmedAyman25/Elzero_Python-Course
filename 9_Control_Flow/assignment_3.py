age = int(input("Enter Your Age ".strip()))

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if age> 10 and age < 100:
    print("You Lived For : ")
    print(f"{months:,} Months.") 
    print(f"{weeks:,} Weeks.") 
    print(f"{days:,} Days.") 
    print(f"{hours:,} Hours.") 
    print(f"{minutes:,} Minutes.") 
    print(f"{seconds:,} Seconds.") 
else:
    print(" Your Age is Out Of range")
