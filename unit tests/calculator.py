def main():
    x = int(input("Enter number"))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n * n

#Need this to prevent automatic execution during import for unit testing
if __name__ == "__main__":
    main()