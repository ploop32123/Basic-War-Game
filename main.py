
import random
from cards.cardfile import Card
from cards.cardfile import SUITS
from cards.cardfile import RANKS
from cards.deck import Deck
from cards.game import Game
from cards.game import Round
from cards.game import HighCardRound

def main():
    print("Hello from cardgame!")


if __name__ == "__main__":
    deck = Deck().basedeck()
    deck1 = deck[26:]
    deck2 = deck[:26]
    
    game = Game()
    
    

    random.shuffle(deck1)
    random.shuffle(deck2)
    
    print(f"Deck 1 before: {[c.rank for c in deck1]}")
    print(f"Deck 2 before: {[c.rank for c in deck2]}")
    while len(deck1) > 0 and len(deck2) > 0:
        game.basegame(deck1, deck2)
    
    print(f"Deck 1 after: {[c.rank for c in deck1]}")
    print(f"Deck 2 after: {[c.rank for c in deck2]}")