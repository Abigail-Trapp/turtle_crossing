from turtle import Screen
import time
from T import T
from level import Level
from cars import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

level = Level()

tim = T()

car = Car()

screen.listen()
screen.onkey(tim.up, "Up")

car_speed = 0.1

#while game is on
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if tim.ycor() > 280:
        tim.goto(0,-280)
        level.update_level()
        car.speedup()

    for x in car.all_cars:
        if x.distance(tim) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()