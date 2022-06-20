from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Super Snake Game")
screen.tracer(0)

# Create the snake
snake = Snake()

# Create moving keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()








screen.exitonclick()