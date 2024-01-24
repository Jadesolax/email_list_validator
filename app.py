import re

# email="james@email.com"


# #create your pattern
# # ^ (begins with ) $ (ends with)
# pattern = re.compile(r"^james")
# pattern = re.compile(r"email.com$")
# pattern = re.compile(r"\w{2,}@\w{4,}.com")
# pattern = re.compile(r"\w+@\w+\.\w+")

# result = pattern.findall(email)



# another example

email = "john@yahoo.com"

pattern = re.compile(r"\w+(@gmail.com | yahoo.com)")

result = pattern.search(email)

print(result)

## \w match all alphabets, numbers (0-9) and underscore

# \D every other item except digit (0-9)

# + (one or more times)

# * (zero or one time)
 
