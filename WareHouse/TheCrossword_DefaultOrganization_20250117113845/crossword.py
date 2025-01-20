'''
CrosswordGrid class to manage the crossword puzzle logic.
'''
class CrosswordGrid:
    def __init__(self, size, clues, answers):
        self.size = size
        self.clues = clues
        self.answers = answers
        self.user_entries = {'across': {}, 'down': {}}
        # Define starting positions for each clue number
        self.start_positions = {
            'across': {
                1: (0, 0),  # Example starting position for clue 1 across
                2: (1, 0),  # Example starting position for clue 2 across
            },
            'down': {
                1: (0, 0),  # Example starting position for clue 1 down
                3: (0, 2),  # Example starting position for clue 3 down
            }
        }
    def validate_word(self, clue_number, direction, word):
        correct_word = self.answers[direction].get(clue_number, "")
        if word.lower() == correct_word:
            self.user_entries[direction][clue_number] = word
            return True
        return False
    def is_complete(self):
        for direction in self.answers:
            for clue_number in self.answers[direction]:
                if self.user_entries[direction].get(clue_number, "") != self.answers[direction][clue_number]:
                    return False
        return True
    def get_word_start_position(self, clue_number, direction):
        return self.start_positions[direction].get(clue_number, None)