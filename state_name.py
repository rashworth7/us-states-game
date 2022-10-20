from turtle import Turtle


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state_name, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(arg=f"{state_name}", align="center", font=("arial", 7, "normal"))
