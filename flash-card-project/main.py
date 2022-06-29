from random import choice
from tkinter import *
import pandas
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("Ariel", 40, "italic")
BIG_FONT = ("Ariel", 60, "bold")
BIG_TEXT_POS = (400, 263)


# ---------------------------- WORD SHOW ------------------------------- #
word_pair = {}

def change():
    global word_pair, flip_timer
    window.after_cancel(flip_timer)#Waits till the 3 seconds are up on the first card

    word_pair = choice(words_dict)
    word = word_pair["French"]
    canvas.itemconfigure(lang_text, text="French", fill="black")
    canvas.itemconfigure(word_text, text=word, fill="black")
    canvas.itemconfigure(canvas_image, image=image_bg_front)

    flip_timer = window.after(3000, func=flip)#Resets the 3 seconds

def flip():
    global word_pair

    canvas.itemconfigure(lang_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=word_pair["English"], fill="white")
    canvas.itemconfigure(canvas_image, image=image_bg_back)

def knows():
    global words_dict
    words_dict.remove(word_pair)
    print(len(words_dict))
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(data)
    change()

# ---------------------------- DATABASE ------------------------------- #
# with open(file="data/french_words.csv") as file:
#     df = pandas.DataFrame(file)
#     dict1 = pandas.DataFrame.to_dict(df)[0]


try:
    with open('data/words_to_learn.csv', encoding='utf-8') as file:
        data = pandas.read_csv(file)
except FileNotFoundError:
    with open('data/french_words.csv', encoding='utf-8') as main_file:
        data = pandas.read_csv(main_file)
        words_dict = data.to_dict(orient='records')
else:
    words_dict = data.to_dict(orient='records')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FLASH")
window.config(padx=35, pady=35, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_bg_front = PhotoImage(file="images/card_front.png")
image_bg_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_bg_front)
canvas.grid(row=0, column=0, columnspan=2)
lang_text = canvas.create_text(400, 150, text="Language", fill="black", font=SMALL_FONT)
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=BIG_FONT)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, highlightthickness=0, command=knows)
right_button.grid(row=1, column=1)
change()




window.mainloop()
