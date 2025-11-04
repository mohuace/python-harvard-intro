#This is for taking command line arguments

import sys

#This will basically get the first argument passed while running the program
# The 0th value in argv is the name of the file itself

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Expecting a command line argument")