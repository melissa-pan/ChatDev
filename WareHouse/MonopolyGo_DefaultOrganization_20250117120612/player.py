'''
Contains the Player class representing a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
    def move(self, steps):
        self.position = (self.position + steps) % 40  # Assuming 40 spaces on the board
    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            self.properties.append(property)
            property.owner = self
    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent