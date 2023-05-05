import random
from tkinter import *
import pandas as pd
from pathlib import Path

FONT = "Ariel"
LANGUAGE_FONT_SIZE = 40
LANGUAGE_FONT_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_FONT_STYLE = "bold"
BACKGROUND_COLOR = "#B1DDC6"

try:
    with open("data/words_to_learn.csv", "r") as file:
        data = pd.read_csv(file)
        data_dictionary = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_dictionary = data.to_dict(orient="records")
finally:
    current_card = {}


# ---------------------------- DELETING THE WORDS THAT THE USER REMEMBERS ------------------------------- #
def user_remembers():
    global current_card
    data_dictionary.remove(current_card)
    words_to_learn_dataframe = pd.DataFrame(data_dictionary)
    words_to_learn_dataframe.to_csv("data/words_to_learn.csv")
    randomize_words()


# ---------------------------- SAVING THE WORDS THAT THE USER FORGOT TO A NEW CSV ------------------------------- #
def user_forgot():
    randomize_words()


# ---------------------------- RANDOMISING THE WORDS ------------------------------- #
def randomize_words():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dictionary)
    canvas.itemconfig(front_image, image=french_image)
    canvas.itemconfig(card_language, text="French")
    canvas.itemconfig(card_word, fill="#000000")
    canvas.itemconfig(card_language, fill="#000000")
    current_french_word = current_card["French"]
    canvas.itemconfig(card_word, text=current_french_word)
    flip_timer = window.after(3000, func=flip_cards)


# ---------------------------- FLIPPING THE CARDS TO ENGLISH ------------------------------- #
def flip_cards():
    global current_card
    current_english_word = current_card["English"]
    canvas.itemconfig(card_language, fill="#FFFFFF")
    canvas.itemconfig(card_word, fill="#FFFFFF")
    canvas.itemconfig(card_word, text=current_english_word)
    canvas.itemconfig(front_image, image=english_image)
    canvas.itemconfig(card_language, text="English")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=900, height=626)
window.title("Flashy")
flip_timer = window.after(3000, func=flip_cards)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
french_image = PhotoImage(file="images/card_front.png")
english_image = PhotoImage(file="images/card_back.png")
front_image = canvas.create_image(400, 263, image=french_image)

# Language Text
card_language = canvas.create_text(400, 150, text="French", font=(FONT, LANGUAGE_FONT_SIZE, LANGUAGE_FONT_STYLE))

# Word Text
card_word = canvas.create_text(400, 263, text=data["French"][0], font=(FONT, WORD_FONT_SIZE, WORD_FONT_STYLE))

canvas.grid(row=0, column=0, columnspan=2)

tick_image = PhotoImage(file="images/right.png")
correct_button = Button(image=tick_image, highlightthickness=0, borderwidth=0, command=user_remembers)
correct_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=user_forgot)
wrong_button.grid(row=1, column=0)

randomize_words()
words_to_learn = data_dictionary.copy()
window.mainloop()
