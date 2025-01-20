'''
Handles the graphical user interface for the Blackjack game.
'''
import tkinter as tk
from blackjack_game import BlackjackGame
class BlackjackGUI:
    def __init__(self):
        self.game = BlackjackGame()
        self.root = tk.Tk()
        self.root.title("Blackjack")
        self.create_widgets()
    def create_widgets(self):
        self.player_label = tk.Label(self.root, text="Player's Hand:")
        self.player_label.pack()
        self.dealer_label = tk.Label(self.root, text="Dealer's Hand:")
        self.dealer_label.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.hit_button = tk.Button(self.root, text="Hit", command=self.handle_hit)
        self.hit_button.pack()
        self.stand_button = tk.Button(self.root, text="Stand", command=self.handle_stand)
        self.stand_button.pack()
        self.double_down_button = tk.Button(self.root, text="Double Down", command=self.handle_double_down)
        self.double_down_button.pack()
        self.update_display()
    def update_display(self):
        player_hand = ', '.join(f"{card.rank} of {card.suit}" for card in self.game.player_hand.cards)
        dealer_hand = ', '.join(f"{card.rank} of {card.suit}" for card in self.game.dealer_hand.cards)
        self.player_label.config(text=f"Player's Hand: {player_hand} (Value: {self.game.player_hand.calculate_value()})")
        self.dealer_label.config(text=f"Dealer's Hand: {dealer_hand} (Value: {self.game.dealer_hand.calculate_value()})")
        self.result_label.config(text="")
    def handle_hit(self):
        self.game.player_hit()
        if self.game.player_hand.is_bust():
            self.result_label.config(text="Player busts! Dealer wins!")
            self.disable_buttons()
        else:
            self.update_display()
    def handle_stand(self):
        self.game.player_stand()
        self.update_display()
        winner = self.game.determine_winner()
        self.result_label.config(text=winner)
        self.disable_buttons()
    def handle_double_down(self):
        winner = self.game.double_down()
        self.update_display()
        self.result_label.config(text=winner)
        self.disable_buttons()
    def disable_buttons(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_down_button.config(state=tk.DISABLED)
    def run(self):
        self.root.mainloop()