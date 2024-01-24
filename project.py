import re
import os

pattern = re.compile(r"\w+@(gmail.com|yahoo.com|hotmail.com)")

accepted_emails = []

## open the inventory file for reading
## other modes w = write (create or recreate) r = read, a = append
foobject = open("inventory.txt", "r")

results = foobject.readlines()

# if = open(accepted_users.txt, "r")

# results + foobject.readlines()

if os.path.exists("accepted_users.txt"):
    os.remove("accepted_users.txt")


f = open("accepted_users.txt", "a")

f.write("Firstname,Lastname,Email,Username\n")

for result in results:
    if result != "Firstname,Lastname,Email,Username\n":
        pattern_result=pattern.search(result)
        
        if pattern_result == None:
            
            accepted_emails.append(result)

            f = open("accepted_users.txt", "w")

            f.write(result)

print(accepted_emails)


