import random
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        rX = random.randint(-280,280)
        rY = random.randint(-280,280)
        self.goto(rX,rY)
        