'''
Contains the Property class representing a property on the board.
'''
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
    def buy(self, player):
        if self.owner is None:
            player.buy_property(self)
    def charge_rent(self, player):
        if self.owner is not None and self.owner != player:
            player.pay_rent(self)