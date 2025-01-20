'''
Represents a deck of cards.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()