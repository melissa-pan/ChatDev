'''
GUI management for the 2048 game using tkinter.
'''
import tkinter as tk
from game2048 import Game2048
class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("2048 Game - 10x10 Grid")
        self.canvas_size = 800  # Increase canvas size
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()
        self.root.bind("<Key>", self.on_key_press)
        self.draw_grid()
    def draw_grid(self):
        self.canvas.delete("all")
        cell_size = self.canvas_size // self.game.size
        for r in range(self.game.size):
            for c in range(self.game.size):
                value = self.game.grid[r][c]
                x0, y0 = c * cell_size, r * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.get_color(value))
                if value != 0:
                    self.canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=str(value), font=("Arial", 24, "bold"))  # Increase font size
    def get_color(self, value):
        colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")
    def update(self):
        self.draw_grid()
        if not self.game.can_move():
            self.canvas.create_text(self.canvas_size / 2, self.canvas_size / 2, text="Game Over", font=("Arial", 32, "bold"), fill="red")
            self.root.unbind("<Key>")  # Disable further key presses
    def on_key_press(self, event):
        key_map = {
            'Up': 'up',
            'Down': 'down',
            'Left': 'left',
            'Right': 'right'
        }
        if event.keysym in key_map:
            self.game.move(key_map[event.keysym])
            self.update()
    def run(self):
        self.root.mainloop()