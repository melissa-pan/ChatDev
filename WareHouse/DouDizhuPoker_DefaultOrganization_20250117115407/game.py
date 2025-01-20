'''
Contains the Game class which manages the overall game logic.
'''
from player import Player
from card import Deck
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2"), Player("Player 3")]
        self.landlord = None
        self.current_player_index = 0
        self.bidding_phase = True
        self.highest_bid = 0
        self.deal_cards()
    def deal_cards(self):
        self.deck.shuffle()
        for i in range(17):
            for player in self.players:
                player.add_card(self.deck.deal_card())
    def bid_for_landlord(self, player_index, bid):
        if bid > self.highest_bid:
            self.highest_bid = bid
            self.landlord = self.players[player_index]
    def finalize_landlord(self):
        if self.landlord is None:
            self.landlord = self.players[0]  # Default to first player if no bids
        self.landlord.add_landlord_cards(self.deck.deal_card(), self.deck.deal_card(), self.deck.deal_card())
        self.bidding_phase = False
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 3
    def check_win(self):
        for player in self.players:
            if player.has_won():
                return player
        return None
    def validate_play(self, cards):
        # Example logic for validating a single card play
        if len(cards) == 1:
            return True  # A single card is always a valid play
        # Example logic for validating a pair
        if len(cards) == 2 and cards[0].rank == cards[1].rank:
            return True
        # Add more rules for other combinations like triples, straights, etc.
        # Example logic for validating a triple
        if len(cards) == 3 and cards[0].rank == cards[1].rank == cards[2].rank:
            return True
        # Example logic for validating a straight (simplified)
        if len(cards) >= 5:
            sorted_cards = sorted(cards, key=lambda card: "34567890JQKA2".index(card.rank))
            for i in range(len(sorted_cards) - 1):
                if "34567890JQKA2".index(sorted_cards[i + 1].rank) - "34567890JQKA2".index(sorted_cards[i].rank) != 1:
                    return False
            return True
        return False  # Return False if no valid combination is found