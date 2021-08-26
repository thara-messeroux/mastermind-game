'''
CS5001
Spring 2021
Final Project : Mastermind Game Point
Thara Messeroux

Purpose: Gives the position of an object for the Mastermind game, which is a coding-breaking board game for two players.

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)
