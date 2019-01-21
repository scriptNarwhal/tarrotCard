"""
Create a tarrot card or a deck of tarrot cards
"""
import random

# expose all methods & variables to the world
major_arcana_cnames = ("The Magician", "The High Priestess", "The Empress", 
    "The Emperor", "The Hierophant", "The Lovers", "The Chariot", 
    "Strength", "The Hermit", "Wheel of Fortune", "Justice", 
    "The Hanged Man", "Death", "Temperance", "The Devil", 
    "The Tower", "The Star", "The Moon", "The Sun", "Judgement", 
    "The World", "The Fool")
major_arcana_ranks = ("I","II","III","IV", "V","VI","VII","VIII","IX",
        "X", "XI","XII","XIII","XIV","XV","XVI","XVII", "XVIII","XIX",
        "XX", "XXI",None)
minor_arcana_cnames = ("A","2","3","4","5","6","7","8","9","10", 'Jack', 'Knight', 'Queen', 'King')
suites = ("Cups", "Swords", "Wands", "Penticles")
def getRandomTarrotCard():
    """Return a random Tarrot card object"""
    major_or_minor = random.randint(0,1)
    card_choice = 0

    if major_or_minor == 0:
        suite = random.choice(suites)
        card_choice = random.randint(0,13)
    else:
        suite = None
        card_choice = random.randint(0,21)

    return TarrotCard(card_choice, suite)

def getTarrotDeck() -> list:
    """ Return a whole Tarrot Deck, a python list of TarrotCard objects """
    deck = []

    for suite in suites:
        for value in range(14):
            deck.append(TarrotCard(value, suite))

    for value in range(22):
        deck.append(TarrotCard(value, None))
    
    return deck

class TarrotCard:
    """ Create a single tarrot card, requires a value and a suite, suite can be None"""
    def __init__(self, value, suite):

        if suite:
            self.name = minor_arcana_cnames[value] + " of " + suite 
            self.suite = suite
            self.value = value + 1
            self.rank = minor_arcana_cnames[value]
            self.arcana = "Minor"
            self.reversed = False
        else:
            self.name = major_arcana_cnames[value] + " " + str(major_arcana_ranks[value])
            self.suite = suite
            self.value = value + 1
            self.rank = major_arcana_ranks[value]
            self.arcana = "Major"
            self.reversed = False
