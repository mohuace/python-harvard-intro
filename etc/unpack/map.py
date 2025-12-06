def main():
    yell("This", "is", "CS50")

# This function takes dynamic number of arguments
def yell(*words):
    # Map function applies the function (given as first argument)
    # to each item of the iterable (given as second argument)
    # Here we are applying str.upper to each word in words
    upper = map(str.upper, words)
    # Finally unpacking the upper map and passing it to print
    print(*upper)

if __name__ == "__main__":
    main()