from tkinter import*
import pandas
import random
import os
# path_images = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images"
# path = os.getcwd()
# print(path_images)


FONT_SIZE_SM = 10
FONT_SIZE_MD = 15
FONT_SIZE_STD = 20
FONT_SIZE_LG = 30
FONT_SIZE_XLG = 40
FONT_SIZE_XXLG = 80
FONT = "Courier"
BACKGROUND_COLOUR = "#B1DDC6"

YELLOW = "#FAFF00"
RED = "#FF3F00"
WHITE = "#FFFFFF"

current_card={}
words_to_learn={}

try:
    df = pandas.read_csv("/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/data/spanish.csv")
    words_to_learn = original_data.to_dict(orient="records")
# print(df)
else:
    words_to_learn = df.to_dict(orient="records")
# print(words_to_learn)


window = Tk()
window.title("FLASH CARDS")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)

IMAGE_FRONT_URL = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images/card_front.png"
IMAGE_BACK_URL = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images/card_back.png"
BUTTON_WRONG = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images/wrong.png"
BUTTON_RIGHT = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images/right.png"
SPANISH_FLAG = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images/spanish_flag.png"
UK_FLAG = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/images/UK.png"
TO_LEARN = "/Users/edwardmadziwa/Desktop/Python/ANGELA YU/Intermidiate/LANGUAGE_FLASH_CARDS/data/"

def next_card():
    global current_card
    global flip_timer
    # Cancels the timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_tittle, text="")
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill=RED)
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_tittle, text="")
    canvas.itemconfig(card_word, text=current_card['English'], fill=WHITE)
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    words_to_learn.remove(current_card)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv(f"{TO_LEARN}words_to_learn.csv", index=False)
    next_card()


flip_timer = window.after(5000, func=flip_card)


# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOUR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
front_img = PhotoImage(file=SPANISH_FLAG)
back_image = PhotoImage(file=UK_FLAG)
card_background = canvas.create_image(400, 263, image=front_img)
card_tittle = canvas.create_text(500, 200, text="", fill=RED, font=(FONT, FONT_SIZE_XLG, "italic"))
card_word = canvas.create_text(500, 263, text="", fill=RED, font=(FONT, FONT_SIZE_XLG, "bold"))

wrong_image = PhotoImage(file=BUTTON_WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=BUTTON_RIGHT)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()





