'''
GUI class that handles the graphical user interface using tkinter.
'''
import tkinter as tk
class GUI:
    def __init__(self, choice_callback):
        self.choice_callback = choice_callback
        self.window = self.create_window()
        # Removed self.window.mainloop() from here
    def create_window(self):
        window = tk.Tk()
        window.title("Interactive Storytelling Game")
        self.text_area = tk.Label(window, wraplength=400, justify="left")
        self.text_area.pack(pady=20)
        self.choice_buttons = []
        return window
    def update_display(self, text, choices):
        self.text_area.config(text=text)
        for button in self.choice_buttons:
            button.destroy()
        self.choice_buttons = []
        for choice in choices:
            button = tk.Button(self.window, text=choice, command=lambda c=choice: self.choice_callback(c))
            button.pack(pady=5)
            self.choice_buttons.append(button)
    def start_gui(self):
        self.window.mainloop()