'''
Contains the GUI class for managing the graphical user interface.
'''
import tkinter as tk
from game import Game
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Dou Dizhu")
        self.setup_ui()
    def setup_ui(self):
        self.info_label = tk.Label(self.root, text="Welcome to Dou Dizhu!")
        self.info_label.pack()
        self.play_button = tk.Button(self.root, text="Play", command=self.play_turn)
        self.play_button.pack()
        self.bid_button = tk.Button(self.root, text="Bid", command=self.bid_for_landlord)
        self.bid_button.pack()
    def bid_for_landlord(self):
        # Implement bidding logic
        for i, player in enumerate(self.game.players):
            bid = int(self.root.simpledialog.askstring("Input", f"{player.name}, enter your bid (0 to pass):"))
            self.game.bid_for_landlord(i, bid)
        self.game.finalize_landlord()
        self.info_label.config(text=f"{self.game.landlord.name} is the landlord!")
    def play_turn(self):
        if self.game.bidding_phase:
            self.info_label.config(text="Bidding phase is not complete.")
            return
        winner = self.game.check_win()
        if winner:
            self.info_label.config(text=f"{winner.name} wins!")
        else:
            self.game.next_turn()
            self.info_label.config(text=f"{self.game.players[self.game.current_player_index].name}'s turn")
    def run(self):
        self.root.mainloop()