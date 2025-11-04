import random

cards = ["Jack", "King", "Queen"]

def main():
    #Seed function will give a defined result always.
    #The random output will give a random result but seed defines that
    # every run of this function would return the same result.

    random.seed(45)

    #Picking 2 cards randomly out of the list.
    print(random.choices(cards, k = 2))


main()