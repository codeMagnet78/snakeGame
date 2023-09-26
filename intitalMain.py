from turtle import Screen, Turtle
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sname Game")
screen.tracer(0) #switching off the tracer so the snake is not gittery

starting_position = [(0,0), (-20,0), (-40,0)]

segments = []

# Create Snake
for postion in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(postion)
    segments.append(new_segment)


# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.3)

    for seg_num in range(len(segments) -1, 0, -1): #range(start, stop, step)
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)    
       

screen.exitonclick()