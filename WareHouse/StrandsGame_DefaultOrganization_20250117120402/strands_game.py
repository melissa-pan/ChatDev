'''
Contains the StrandsGame class that manages the game logic.
'''
class StrandsGame:
    def __init__(self):
        self.strands = []
        self.correct_combinations = ["hello", "world", "python", "programming"]
        self.current_combination = ""
        self.formed_combinations = set()
    def load_strands(self, file_path="strands.txt"):
        # Load strands from an external file
        try:
            with open(file_path, 'r') as file:
                self.strands = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Strands file not found. Using default strands.")
            self.strands = ["he", "llo", "wor", "ld", "py", "thon", "pro", "gram", "ming"]
    def check_combination(self, combination):
        # Check if the combination is valid
        if combination in self.correct_combinations and combination not in self.formed_combinations:
            self.formed_combinations.add(combination)
            return True
        return False
    def is_complete(self):
        # Check if all correct combinations have been formed
        return self.formed_combinations == set(self.correct_combinations)