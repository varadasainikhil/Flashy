import random
from tkinter import *
import pandas as pd

FONT = "Ariel"
LANGUAGE_FONT_SIZE = 40
LANGUAGE_FONT_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_FONT_STYLE = "bold"
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
data_dictionary = data.to_dict(orient="records")


# ---------------------------- RANDOMISING THE WORDS ------------------------------- #
def randomize_words():
    current_card = random.choice(data_dictionary)
    current_french_word = current_card["French"]
    current_english_word = current_card["English"]
    canvas.itemconfig(card_word, text=current_french_word)
    print(current_french_word)
    print(current_english_word)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=900, height=626)
window.title("Flashy")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
french_image = PhotoImage(file="images/card_front.png")
front_image = canvas.create_image(400, 263, image=french_image)

# French Text
card_language = canvas.create_text(400, 150, text="French", font=(FONT, LANGUAGE_FONT_SIZE, LANGUAGE_FONT_STYLE))

card_word = canvas.create_text(400, 263, text=data["French"][0], font=(FONT, WORD_FONT_SIZE, WORD_FONT_STYLE))

canvas.grid(row=0, column=0, columnspan=2)

tick_image = PhotoImage(file="images/right.png")
correct_button = Button(image=tick_image, highlightthickness=0, borderwidth=0, command=randomize_words)
correct_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=randomize_words)
wrong_button.grid(row=1, column=0)

window.mainloop()
