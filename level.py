from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 1
        self.penup()
        self.hideturtle()
        self.sety(260)
        self.setx(-220)
        self.display_level()

    def display_level(self):
        self.write(f"Level: {self.number}", align="center", font=("Courier", 15, "bold"))

    def update_level(self):
        self.number += 1
        self.clear()
        self.display_level()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))