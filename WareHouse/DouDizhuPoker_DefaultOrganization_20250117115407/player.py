'''
Contains the Player class representing a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def add_card(self, card):
        self.hand.append(card)
    def add_landlord_cards(self, *cards):
        self.hand.extend(cards)
    def play_cards(self, cards):
        if all(card in self.hand for card in cards):
            for card in cards:
                self.hand.remove(card)
            return cards
        return None
    def has_won(self):
        return len(self.hand) == 0