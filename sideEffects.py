
#Side effect is...something that gets changed while our function is running

emoticon = ":("

def main():
    
    #If this is not mentioned, a local variable called emoticon will be created
    global emoticon

    say("Is Anyone here?")

    #Trying to do a side effect where changing the emoticon
    #This creates a local copy (if global is not mentioned)
    emoticon = ":D"



    say("Oh Hi")


#Printing to the terminal is a side effect
def say(phrase):
    print(phrase + " " + emoticon)


main()