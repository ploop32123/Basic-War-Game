import random
from .cardfile import Card
from .cardfile import SUITS
from .cardfile import RANKS
from .deck import Deck

class Round:
    def resolve_round(self) -> int:
        raise NotImplementedError("Subclasses must implement resolve_round()")

class HighCardRound(Round):
    def __init__(self, card1, card2) -> None:
        self.card1 = card1
        self.card2 = card2
    def resolve_round(self) -> int:
        if self.card1 > self.card2:
            return 1
        if self.card1 < self.card2:
            return 2
        if self.card1 == self.card2:
            return 0

class Game:
    
    def __init__(self):
        self.cardpot = []
    
    
    
    
    def basegame(self, player1deck, player2deck):
        
        if len(player1deck) == 0:
            print("Player 2 wins the game!")
            return
        elif len(player2deck) == 0:
            print("Player 1 wins the game!")
            return
        
        rounds = HighCardRound(player1deck[0], player2deck[0])
        result = rounds.resolve_round()
        if result == 1:
            offcard = player2deck.pop(0)
            self.cardpot.append(offcard)
            soffcard = player1deck.pop(0)
            self.cardpot.append(soffcard)
            player1deck.extend(self.cardpot)
            self.cardpot = []
            
        if result == 2:
            soffcard = player1deck.pop(0)
            self.cardpot.append(soffcard)
            offcard = player2deck.pop(0)
            self.cardpot.append(offcard)
            player2deck.extend(self.cardpot)
            self.cardpot = []
        
        if result == 0:
            self.handle_war(player1deck,player2deck)
                
                
    def handle_war(self, player1deck, player2deck):
        cards_to_pile = min(4, len(player1deck), len(player2deck))
        player1topile = player1deck[:cards_to_pile]
        self.cardpot.extend(player1topile)
        del player1deck[:cards_to_pile]
        player2topile = player2deck[:cards_to_pile]
        del player2deck[:cards_to_pile]
        self.cardpot.extend(player2topile)
        
        if cards_to_pile == 1:
            player1pile = min(4, len(player1deck))
            player2pile = min(4, len(player2deck))
            if player1pile > player2pile:
                return 1
            elif player1pile < player2pile:
                return 2
            else : self.basegame(player1deck, player2deck)
        if cards_to_pile != 4:
            score = HighCardRound(player1topile[-1], player2topile[-1])
            if score == 1:
                offcard = player2deck.pop(0)
                self.cardpot.append(offcard)
                soffcard = player1deck.pop(0)
                self.cardpot.append(soffcard)
                player1deck.extend(self.cardpot)
                self.cardpot = []
            
            if score == 2:
                soffcard = player1deck.pop(0)
                self.cardpot.append(soffcard)
                offcard = player2deck.pop(0)
                self.cardpot.append(offcard)
                player2deck.extend(self.cardpot)
                self.cardpot = []
        
            if score == 0:
                self.handle_war(player1deck,player2deck)
            
            
            
        self.basegame(player1deck, player2deck)
        
            
