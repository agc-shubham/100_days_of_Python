from turtle import Screen
import turtle
import pandas as pd

screen = Screen()
screen.title("U.S.A states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv('50_states.csv')
states = df.state.to_list()


guessed_states = []
while len(guessed_states) <= 50:

    answer_state = screen.textinput(title= f'{len(guessed_states)}/50 States',prompt='Enter another state!')
    answer_state = answer_state.title()
    
    if answer_state == "Exit":
        
        missing_states = [state for state in states if state not in guessed_states ]
        # for state in states:
        
        #     if state not in guessed_states:
        #         missing_states.append(state)

        # break

    if answer_state in states:
        guessed_states.append(answer_state)
        # print('yes')
        row = df[df['state']==answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(row['x']),int(row['y']))
        t.write(answer_state)

dfnew = pd.DataFrame(missing_states,columns=[['States']])
dfnew.to_csv('missing_sates.csv',index=False)

# def get_mouse_click_cor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

# screen.exitonclick()
