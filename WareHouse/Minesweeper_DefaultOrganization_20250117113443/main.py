'''
This is the main module to start the Minesweeper game.
'''
import tkinter as tk
from gui import MinesweeperGUI
def main():
    root = tk.Tk()
    app = MinesweeperGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()