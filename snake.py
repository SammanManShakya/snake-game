from turtle import *
positions = [(0,0), (0,-20), (0,-40)]
x = 0
y = 0
move_distance = 20
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.direction = "east"
        self.head = self.snake_body[0]

    def create_snake(self):
        for nums in positions:
            self.add_segment(nums)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def add_segment(self, position):

        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def move(self):
        for num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[num].goto(self.snake_body[num - 1].xcor(), self.snake_body[num - 1].ycor())

        self.snake_body[0].forward(move_distance)

    def left(self):
        if self.direction != "east" and self.direction != "west":
            if self.direction == "north":
                self.snake_body[0].left(90)
            else:
                self.snake_body[0].right(90)

            self.direction = "west"

    def right(self):
        if self.direction != "east" and self.direction != "west":
            if self.direction == "north":
                self.snake_body[0].right(90)

            else:
                self.snake_body[0].left(90)

            self.direction = "east"

    def up(self):
        if self.direction != "north" and self.direction != "south":
            if self.direction == "west":
                self.snake_body[0].right(90)
            else:
                self.snake_body[0].left(90)

            self.direction = "north"

    def down(self):
        if self.direction != "north" and self.direction != "south":
            if self.direction == "west":
                self.snake_body[0].left(90)
            else:
                self.snake_body[0].right(90)

            self.direction = "south"

    def reset(self):
        for snakes in self.snake_body:
            snakes.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
