'''
NarrativeSegment class that represents a segment of the story.
'''
class NarrativeSegment:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices
    def display(self):
        # Return the narrative text
        return self.text
    def get_choices(self):
        # Return the available choices
        return self.choices