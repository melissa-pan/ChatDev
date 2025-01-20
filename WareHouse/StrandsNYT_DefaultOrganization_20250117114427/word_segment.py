'''
Defines the WordSegment class for the NYT Strands puzzle game.
'''
class WordSegment:
    def __init__(self, text):
        self.text = text
    def get_text(self):
        return self.text