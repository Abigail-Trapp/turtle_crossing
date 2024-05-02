from turtle import Turtle
import random

RANDOM_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE = 5
MOVE_DISTANCE = 5

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(RANDOM_COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250,270))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speedup(self):
        self.car_speed += 2