# This extracts username from a twitter url.

import re

url = input("Enter URL: ").strip()

# This is too stringent. Can't type twitter.com only without https.
# Not good user experience
# username = url.replace("https://twitter.com/", "")

# print(username)

# Using regular expressions.
# We can use re.sub which substitutes a string (pattern) with another string.

# Accounting for both http and https using ?
# Adding \. for telling python that its a literal dot
# www. is also optional so its grouped and a question mark is added right after
# The http:// or https:// entirely is kept optional as well
# This however wont change the input if we type something completely random like www.google.com/mohit
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(username)

# Therefore, we can keep it like this itself.
# Using ?: for www. in the paranthesis for having grouping but not capturing that in the result.
matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)", url, re.IGNORECASE)

# If there is match, only then print the grouped value, basically the username
if matches:
    print(matches.group(1))