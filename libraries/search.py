#Libraries / Modules are python files that we can import
# in our file.
# Packages consists of multiple modules / libraries.
# We need to create an __init__.py file for python to know we are creating
# a package. Hence, museum folder is a package.

from museum.artist import get_artist

def main():
    get_artist()

main()