from turtle import Screen
import time ;
from snake import Snake
from food import Food
from scoreBoard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn of screen to refresh on it on because of the delay animation of moving snake

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

# screen.update() #updating screen after snake is created
game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    
    # Snake Collide with food
    if snake.head.distance(food) < 15 :
        score.increase_score()
        snake.extend()
        food.refresh()
    
    # Repostion to opposite side if collide with wall
    if snake.head.xcor() > 280:
        snake.refreshPosition(-280,snake.head.ycor())
    if snake.head.xcor() < -280:
        snake.refreshPosition(280,snake.head.ycor()) 
    if snake.head.ycor() < -280:
        snake.refreshPosition(snake.head.xcor(),280) 
    if snake.head.ycor() > 280:
        snake.refreshPosition(snake.head.xcor(),-280) 
   
    # Snake Collide with itself
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10 :
            game_over = True
            score.game_over()

screen.exitonclick() # To not close as it run