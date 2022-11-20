from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("50_states.csv")
state = pd.DataFrame(data).to_dict()

state_writer = Turtle()
state_writer.penup()
state_writer.hideturtle()

ekran = Screen()
ekran.setup(725, 491)
ekran.addshape("blank_states_img.gif")
ekran.bgpic("blank_states_img.gif")
ekran.title("U.S. State Game")

true_answers = 0
answers = []

while true_answers < len(state["state"]):
    answer = ekran.textinput(title=f"{true_answers}/50 Correct", prompt="What's another state name ?")
    if answer not in answers:
        for i in range(49):
            if answer.lower() in state["state"][i].lower():
                true_answers += 1
                location = state["x"][i], state["y"][i]
                state_writer.goto(location)
                state_writer.write(arg=state["state"][i])
                answers.append(answer)
        if answer.lower() == "close":
            break

print(f"Your total score is {true_answers}/50")
print("Good bye ")
