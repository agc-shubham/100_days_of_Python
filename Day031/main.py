# ******************** Imports *******************************
from tkinter import *
from numpy import flip
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ********************** Data Ingestion and Functions***********************
current_card = {}
to_learn = {}
try:
    df = pandas.read_csv("data/words_to_learn.csv")
    
except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")
    




# for index, row in df.iterrows():
#     word = {row[0]:row[1]}
#     to_learn.append(word)

# print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=cardfront_img)
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    global current_card
    canvas.itemconfig(canvas_title, text="English",fill="white")
    canvas.itemconfig(canvas_word, text=current_card['English'],fill="white")
    canvas.itemconfig(card_background, image=cardback_img)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
# ********************** Canvas *******************************

window = Tk()
window.title("Flash Card Quiz")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# ******************** Canvas *********************************************

canvas = Canvas(width=800,height=526)
cardfront_img = PhotoImage(file="images/card_front.png")
cardback_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=cardfront_img)
canvas_title = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="English", fill="black", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0, columnspan=2)

# ********************* Buttons *******************************
cross_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cross_image,highlightthickness=0, command=next_card)
cancel_button.grid(row=1,column=0)

tick_image = PhotoImage(file="images/right.png")
okay_button = Button(image=tick_image,highlightthickness=0, command=is_known)
okay_button.grid(row=1,column=1)
next_card()

window.mainloop()