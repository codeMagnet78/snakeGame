from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sname Game")
screen.tracer(0) #switching off the tracer so the snake is not gittery


# Create Snake
snake = Snake()
# Create Food
food = Food()

# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.3)

    snake.snake_move()
    # Controlling the snake
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()