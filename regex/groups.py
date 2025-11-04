import re

locations = {"+1": "US and Canada", "+62": "Indonesia", "+505": "Nicarguna"}

number = input("Enter Number: ")

# If we want to capture the country codes from the entire phone number, its easy to do it
# using regex. We can capture country codes with dynamic lengths. Using normal
# string manipulation, it would be messy to get the country code substring.

# \d means number, we want the code to be between 1 and 3 times.
# Then the number will be in format +0 000-000-0000
# There is way to name the groups. By using ?P<>
pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"

match = re.search(pattern, number)

if match:
    print(f"The country code is of country: {locations[match.group("country_code")]}")

else:
    print("Invalid")