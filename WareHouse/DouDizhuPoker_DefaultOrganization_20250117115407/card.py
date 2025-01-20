'''
Contains the Card and Deck classes for managing cards.
'''
import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{self.rank}{self.suit}"
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in "34567890JQKA2" for suit in "♠♥♦♣"] + [Card("Joker", "Black"), Card("Joker", "Red")]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop() if self.cards else None