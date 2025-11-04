#If there is a syntax error, that is for the programmer to fix
#But for runtime errors, like user giving an input other than number, like a string.
#The program will crash

# x = int(input("Enter a number: "))

# print("The number is", x)

while(True):
    try:
        x = int(input("Enter a number: "))
    
    #There is a way to catch all the errors,
    #but generally not recommended because errors reasons are
    #sometimes swallowed.
    except ValueError:
        #You can print the error
        #print("x is not a number")

        #You can just pass, not do anything when exception comes
        pass

    #If nothing goes wrong, it will go in else. Why do we need this?
    #Because we can define print in try but we know print is not going to cause any exceptions so why to keep there?
    #Also, printing directly after try except block won't work because x is not assigned a value when an error occurs
    else:
        print("The number is:", x)
        break