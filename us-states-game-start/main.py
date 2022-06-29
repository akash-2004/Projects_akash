import turtle

import pandas


def check_answer(user_answer):
    # for state_name in states:
    #     if user_answer.lower() == state_name.lower():
    #         return state_name, True
    # return False
    if user_answer.title() in states:
        return user_answer.title(), True
    return False


def cheat():
    for state_name in data:
        turtle.goto(data[state_name])
        turtle.write(state_name)


def generate_list_to_learn():
    states_to_learn_list = [i for i in states if i not in correct_states]
    states_to_learn = pandas.DataFrame(states_to_learn_list)
    states_to_learn.to_csv("states_to_learn.csv")
    print(states_to_learn)


turtle.hideturtle()
turtle.penup()
screen = turtle.Screen()
# screen.setup(width=600, height=550)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
screen.bgpic(image)
states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].to_list()

# Creating a dictionary with state name as key and coordinates in list form as value
x_coords = states_data["x"].to_list()
y_coords = states_data["y"].to_list()
data = {}
for i in range(len(states)):
    data[states[i]] = (x_coords[i], y_coords[i])

correct_states_score = 0
correct_states = []
while correct_states_score != 50:
    answer_state = screen.textinput(title=f"{correct_states_score}/50 States Correct",
                                    prompt="What's another state's name?")
    if answer_state.lower() == "cheat":
        cheat()
        correct_states_score = 50
        turtle.mainloop()
    elif answer_state.lower() == "exit":
        generate_list_to_learn()
        break
    elif check_answer(answer_state):
        correct_states_score += 1
        state = check_answer(answer_state)
        correct_states.append(state[0])
        turtle.goto(data[state[0]])
        turtle.write(state[0])


