from turtle import Turtle


FONT = ("Arial", 18, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        
        self.score = 0
        self.write(f"Score : {self.score}", align="center", font=FONT)
        
    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=FONT)
    
    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=FONT)