from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sname Game")
screen.tracer(0)  # switching off the tracer so the snake is not gittery


# Create Snake
snake = Snake()
# Create Food
food = Food()
# Scoreboard
scoreboard = Scoreboard()


# Controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.snake_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # Detect wall collision
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
