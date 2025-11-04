def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

#Whenever this file is loaded by python somewhere else (imported in say.py), the main() is going to get
# called
#main()

#We can use this. When this python program is called through command line, only then this
#condition will be true. When importing in other file, it will be false and hence wont run
if __name__ == "__main__":
    main()