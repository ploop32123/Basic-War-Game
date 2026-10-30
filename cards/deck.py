import random
from .cardfile import Card
from .cardfile import SUITS
from .cardfile import RANKS


class Deck:
    def basedeck(self):
        deck = []
        for i in SUITS:
            for u in RANKS:
                deck.append(Card(u, i))
        random.shuffle(deck)
        return deck