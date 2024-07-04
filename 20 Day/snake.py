from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segements = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segements.append(new_segment)
        
    def move(self):
        for seg_num in range(len(self.segements) - 1, 0, -1):
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(x=new_x, y=new_y)
        self.segements[0].forward(20)