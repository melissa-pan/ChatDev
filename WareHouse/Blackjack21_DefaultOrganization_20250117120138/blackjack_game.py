'''
Manages the game logic for Blackjack.
'''
from deck import Deck
from hand import Hand
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_bet = 0
        self.start_new_round()
    def start_new_round(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.player_bet = 10  # Example starting bet
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
    def player_hit(self):
        self.player_hand.add_card(self.deck.deal_card())
    def player_stand(self):
        self.dealer_play()
    def double_down(self):
        self.player_bet *= 2
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_play()  # Dealer plays immediately after doubling down
        # Determine the winner after the dealer plays
        winner = self.determine_winner()
        return winner
    def dealer_play(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        if self.player_hand.is_bust():
            return "Dealer wins!"
        elif self.dealer_hand.is_bust():
            return "Player wins!"
        elif player_value > dealer_value:
            return "Player wins!"
        elif dealer_value > player_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"