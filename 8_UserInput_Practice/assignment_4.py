email = input("Enter your email address: ").strip().lower()
UserName = email[:email.index("@")].capitalize()
WebSite = email[email.index("@")+1:email.index(".")]
Domain = email[email.index(".")+1:]

print(f"Your User Name Is: {UserName}")
print(f"Email Service Provider Is: {WebSite}")
print(f"Top Level Domain Is : {Domain}")