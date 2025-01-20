'''
Represents a player's or dealer's hand.
'''
from card import Card
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        value = sum(card.value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.rank == 'A')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    def is_bust(self):
        return self.calculate_value() > 21