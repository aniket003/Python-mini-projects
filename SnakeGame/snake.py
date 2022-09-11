from turtle import Turtle

START_POSITION=[(0,0),(-20,0),(-40,0)]  # Constant so all caps variable name
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for pos in START_POSITION:
            self.addSegment(pos)
            
    def addSegment(self,position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()  # to not draw the line
        segment.goto(position) 
        self.segments.append(segment) # collection of segments
    
    def extend(self):
        self.addSegment(self.segments[-1].position())
      
    def move(self):
        for seg in range( len(self.segments)-1 , 0 , -1 ):
            
            new_x = self.segments[seg -1].xcor() 
            new_y = self.segments[seg -1].ycor() 
            self.segments[seg].goto(new_x,new_y)
    
        self.head.forward(MOVING_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def refreshPosition(self,x,y):
        self.head.goto(x,y)
        
    