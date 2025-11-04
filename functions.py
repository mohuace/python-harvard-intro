#This is a global variable
emoticon = ":("


def process():

    #Need to specify explicitly that we are trying to access global variable
    global emoticon

    #Trying to access global var
    print("Hey, " + emoticon)

    emoticon = ":)"


def main():
    process()
    print("After process, ", emoticon)


main()