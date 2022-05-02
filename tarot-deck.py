import random

def fortuneTelling():
    myDeck = {}
    cardNumber = random.randint(0, 77)

    with open("tarotCards.txt", 'r') as f:
        for line in f:
            (k, v) = line.split(':')
