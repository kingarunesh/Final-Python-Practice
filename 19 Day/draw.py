from turtle import Turtle, Screen


def move_forward():
    tom.forward(20)

def move_backwards():
    tom.backward(20)
    
def counter_clockwise():
    tom.left(15)

def clockwise():
    tom.right(15)

# def reset_moves():
#     tom.reset()
#     tom.pensize(2)
#     tom.turtlesize(2)

def reset_moves():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


tom = Turtle()
tom.pensize(2)
tom.turtlesize(2)

screen = Screen()
screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=reset_moves, key="c")



screen.exitonclick()