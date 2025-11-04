# random is a library / module
# once you import it, you have access to all its functions
# Basically this imports everything
import random

#Alternative to just import the choice function from random module
from random import choice


# random.choice(seq). This fn takes a sequence of choices and given an output
# with equal probability of their likelihood.
coin = random.choice(["heads", "tails"])

print(coin)

# Generate a random number between 1 and 10. Both are inclusive
ranNum = random.randint(1, 10)
print(ranNum)

# random.shuffle(x). Shuffles the list in place
cards = ["jack", "queen", "spade"]
random.shuffle(cards)
print(cards)