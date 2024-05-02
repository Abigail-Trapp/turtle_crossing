from turtle import Turtle
class T(Turtle):
    def __init__(self):
        super().__init__()
        # set up turtle to starting position
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.setpos(0,-280)

    def up(self):
        self.forward(10)