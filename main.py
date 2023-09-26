from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sname Game")
screen.tracer(0) #switching off the tracer so the snake is not gittery


# Create Snake
snake = Snake()


# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.3)

    snake.snake_move()

screen.exitonclick()