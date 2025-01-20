'''
Contains the GUI class for managing the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
import random
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Monopoly Go!")
        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack()
    def update_display(self):
        info = "\n".join([f"{player.name}: ${player.money}" for player in self.game.players])
        self.info_label.config(text=info)
        self.root.update()
    def prompt_player_action(self, player):
        roll = self.roll_dice()
        player.move(roll)
        property = self.game.board.get_property(player.position)
        if property is not None:
            if property.owner is None:
                if messagebox.askyesno("Buy Property", f"Do you want to buy {property.name} for ${property.price}?"):
                    player.buy_property(property)
            else:
                property.charge_rent(player)
        # Check if the player landed on a chance card space
        chance_positions = [7, 22, 36]  # Example positions for chance cards
        if player.position in chance_positions:
            self.game.board.draw_chance_card(player)
    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)
    def run(self):
        self.root.mainloop()