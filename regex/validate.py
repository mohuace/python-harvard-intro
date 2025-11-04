import re

# Lets try to validate email addresses using standard means.

email = input("Enter your email address: ").strip()

# Will try to split the email into two parts and check whether domain and username are valid
# We can validate this way but if the user types something like "user@.com" it will still be considered valid
# To handle such cases, we can use regular expressions
# try:
#     username, domain = email.split("@")
#     if username and domain and domain.endswith(".com"):
#         print("Valid email address")
#     else:
#         print("Invalid email address")
# except ValueError:
#     print("Invalid email address")



# Using regular expressions

# This is saying: There must be at least one character (.+) before the @ symbol,
# followed by at least one character (.+) before the .com part (\.com).
# The backslash before the dot is necessary because a dot in regex means "any character",
# so we need to escape it to indicate we literally mean a dot.
# And for python to avoid treating \ as an escape character, eg: \n, we use raw string by prefixing the string with r
# But here, mohit@@@example.com will still be considered valid.
# When you don't provide anchors (^ for start and $ for end), re.search will look for the pattern anywhere in the string.
# So, this means that start with any characters, then have @, then any characters, then .com and then nothing else after that.

#if re.search(r"^.+@.+\.com$", email):

# To prevent multiple @ symbols, we are saying that start with any characters except @ ([^@]+), then have a single @,
# then any characters except @ ([^@]+), then .com and then nothing else after that.
# if re.search(r"^[^@]+@[^@]+\.com$", email):

# To be even more restrictive, we can specify what characters are allowed in username and domain.
# So I am allowing only alphanumeric characters and underscores (_) in both username and domain.
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):

# Can use \w to represent alphanumeric characters and underscores
# if re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE):

# To allow subdomains (like mail.example.com), we can modify the domain part to allow an optional subdomain.
# ? makes the preceding group optional (0 or 1 occurrence)
# Username can have dots (.) as well so we have made it optional. 
# That is it can be either word characters or dots before the @ symbol.

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid email address")
else:
    print("Invalid email address")


# re.fullmatch can also be used that ensures the entire string matches the pattern.
# So we don't need to use ^ and $ anchors with fullmatch.