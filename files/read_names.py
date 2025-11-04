# Assuming we already have names.txt created by write_names.py
# This script reads names from names.txt and prints them

with open("names.txt", "r") as file:
    names = file.readlines()


for name in names:
    # This prints each name but adds an extra newline from the file after each name.
    #print(name)

    # Therefore, we can remove the extra newline by stripping from the end.
    print(name.rstrip())  # rstrip() removes trailing whitespace including newlines