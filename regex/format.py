# This is for formatting the name input from users.

import re

name = input("Enter your name: ").strip()

# The name can be typed in two ways: Mohit Thaker or Thaker, Mohit

# This means the string can start with any number of characters followed by a comma and then any number of characters
# Adding groupings, (), also allows us to capture the data into the variable matches. So we are capture last name and first name
# The space after comma is optional
matches = re.search("^(.+), *(.+)$", name)

if matches:
    name = f"{matches.group(2)} {matches.group(1)}"


print(f"Hello, {name}")

