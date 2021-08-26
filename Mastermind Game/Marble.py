'''
CS5001
Spring 2021
Final Project : Mastermind Game Marble
Thara Messeroux

Purpose: Programs a marble for the Mastermind game, which is a coding-breaking board game for two players.

'''
import turtle
from Point import Point

MARBLE_RADIUS = 15

class Marble:
    def __init__(self, position, colors, color = None, draw = True, size = MARBLE_RADIUS):
        self.pen = self.new_pen()
        if color: # Drawing the marbles
            self.color = color
            self.is_empty = False
        else:
            self.color = None
            self.is_empty = True
        self.colors = colors
        self.position = position
        self.visible = False
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing
        if draw and self.is_empty: self.draw_empty() # look at default values
        elif draw: self.draw()
        
    def new_pen(self): 
        return turtle.Turtle()

    def set_color(self, color):
        self.color = color
        self.is_empty = False

    def get_color(self):
        return self.color

    def draw(self):
        # if self.visible and not self.is_empty:
            # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        if abs(x - self.position.x) <= self.size+3 and \
           abs(y - self.position.y) <= self.size+3:
            return True
        return False


    def change_color(self, x, y):
        if self.clicked_in_region(x, y):
            current_color = self.get_color
            current_index = colors.index(current_color)
            new_index = (current_index + 1) % len(colors)
            self.set_color(colors[new_index])

def main():
    pass
    #marble = Marble(Point(100,100), "blue")
    #marble.draw_empty()
    #k = input("enter something here and I'll fill the marble > ")
    #marble.draw()
    #k = input("enter something here and I'll erase the marble > ")
    #marble.erase()

if __name__ == "__main__":
    main()
