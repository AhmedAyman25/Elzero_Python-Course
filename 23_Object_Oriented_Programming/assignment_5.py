# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    pass
        
# Create Moderators Class Here
class Moderators(Admins):
    pass

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator