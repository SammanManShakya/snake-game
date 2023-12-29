from turtle import *
import random
import time
from snake import *
from food import *
from scoreboard import *

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# head = Turtle(shape="square")
# head.color("white")
# body = Turtle(shape="square")
# body.color("white")
# tail = Turtle(shape="square")
# tail.color("white")
# x = 0
# y = 0
#
# snake_body = []
# for _ in range (3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.penup()
#     snake.setpos(x,y)
#     snake_body.append(snake)
#     x -= 20

screen.update()
game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_board()
        snake.reset()


    for segment in snake.snake_body[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset_board()
            snake.reset()



screen.exitonclick()