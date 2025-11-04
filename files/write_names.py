
name = input("Enter a name: ")

# Open function will create (if not exists) or overwrite the file and write the name into it
# file = open("names.txt", "w")

# To prevent overwriting, use "a" mode to append the name to the file
# file = open("names.txt", "a")

# file.write(f"{name}\n")
# file.close()

# We don't need to explicitly close the file when using 'with' statement
# The file is automatically opened and closed within this context, that is the block of code under 'with'
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

print("Name saved to names.txt")

