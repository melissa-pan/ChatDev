'''
Utility functions for the Checkers game.
'''
def position_to_coordinates(position):
    return position[1] * 100 + 50, position[0] * 100 + 50
def coordinates_to_position(coordinates):
    return coordinates[1] // 100, coordinates[0] // 100