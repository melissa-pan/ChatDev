'''
GameState class that tracks the player's progress and current segment.
'''
from narrative_segment import NarrativeSegment
class GameState:
    def __init__(self):
        self.relationships = {}
        self.items = []
        self.current_segment = None
        self.choice_map = {
            "Start": NarrativeSegment("You embark on your journey.", ["Go North", "Go South"]),
            "Go North": NarrativeSegment("You head north into the forest.", ["Explore deeper", "Return to path"]),
            "Go South": NarrativeSegment("You travel south to the village.", ["Talk to villagers", "Visit market"]),
            # Add more choices and corresponding narrative segments as needed
        }
    def update_state(self, choice):
        # Update relationships, items, and current segment based on choice
        if choice in self.choice_map:
            self.current_segment = self.choice_map[choice]
            # Update relationships or items if necessary
            # Example: self.relationships["villager"] = "friendly"
            # Example: self.items.append("map")
    def get_current_segment(self):
        # Return the current narrative segment
        return self.current_segment