'''
Contains the Board class representing the game board and its properties.
'''
from property import Property
import random
class Board:
    def __init__(self):
        self.properties = [
            Property("Mediterranean Avenue", 60, 2),
            Property("Baltic Avenue", 60, 4)
            # Add more properties as needed
        ]
        self.chance_cards = [
            ("Advance to Go", self.advance_to_go),
            ("Bank pays you dividend of $50", self.bank_pays_dividend)
            # Add more chance cards as needed
        ]
    def get_property(self, position):
        if position < len(self.properties):
            return self.properties[position]
        else:
            return None  # or handle other types of spaces
    def draw_chance_card(self, player):
        card = random.choice(self.chance_cards)
        card[1](player)
    def advance_to_go(self, player):
        player.position = 0
        player.money += 200
    def bank_pays_dividend(self, player):
        player.money += 50