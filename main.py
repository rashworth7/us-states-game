import csv
import turtle
import pandas
from state_name import State

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=730, height=490)

turtle.shape(image)

score = 0
correct_guesses = []

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
print(data_dict)

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name")
    answer_state_l = answer_state.lower()
    answer_state_c = answer_state.capitalize()
    with open("50_states.csv") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if answer_state_l == row[0].lower() and answer_state.capitalize() not in correct_guesses:
                x_cor = int(row[1])
                y_cor = int(row[2])
                state = State()
                state.write_state(answer_state_c, x_cor, y_cor)
                score += 1
                correct_guesses.append(answer_state_c)




# game_is_on = True
# while game_is_on:
#     answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state name")
#     for state in data_dict:
#         if state == answer_state:
#             num_correct += 1
#             print("yay")


    # else:
    #     coordinates =

turtle.mainloop()
