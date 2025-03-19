# Match Any Email 
# [A-z0-9\.]+@+[A-z]+\.+[A-z]+ 
# ^[A-z0-9\.]+@+[A-z]+\.+[A-z]+$ 
# ^ Start of String 
# $ End of String
################################################################################
# Match Emails that ends with `com and net`
# [A-z0-9\.]+@+[A-z]+\.+(com|net)
# ^[A-z0-9\.]+@+[A-z]+\.+(com|net)$
################################################################################
# Match URLs
#(https?://)(www\.)?(\w+)\.(org|com)
###############################################################################
# . -> means match all chars except the new line (\n)

import re

# search() -> return First Match Only
# findall() -> return a list of matches and Empty list if no matches
# split(Pattern, String, Maxsplit) -> return a list of elements splitted on each match
# sub(Pattern, Replace, String, ReplaceCount) -> replace matches with what you want
my_search = re.search(r"[A-Z]{2}","AAhmedaymaNN")
print(my_search)

my_Text = "I Love Python"

new_list = re.split(r"\s",my_Text)

print(new_list)

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub("\s", "-", my_Text, flags=re.IGNORECASE & re.MULTILINE)

print(new_string) 