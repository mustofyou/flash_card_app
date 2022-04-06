import random

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
current_card = {}


#word_list

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    print("no words_to_learn file")
    data = pandas.read_csv("data/french_words.csv")
    data.to_csv('data/words_to_learn.csv', index=False)
else:
    print("there is a words_to_learn file")

print("sen anan yani")

to_learn = data.to_dict(orient="records") #orient is the parameter to determine the dict type eg record is as follow.
print()


#functions
def update_new_set(word):
    global data
    print("deleting the word")
    to_learn.remove(word)


    # copy the original file to the new file and use this func inside the next_card func to delete words as the user hits the next button

def next_card():
    global current_card, flip_timer_id
    window.after_cancel(flip_timer_id)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_card_image, image=card_front)
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=current_card["French"])
    update_new_set(current_card)
    flip_timer_id = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(canvas_card_image, image=card_back)
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=current_card["English"])



#tkinter window
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

flip_timer_id = window.after(3000, func=flip_card)

#images
card_front =  PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")

#canvas
canvas = Canvas(width = 800, height = 526)
canvas_card_image = canvas.create_image(400,263,image=card_front) #card
canvas_title = canvas.create_text(400,150,text="",font=("ariel",40,"italic"))
canvas_word = canvas.create_text(400,263,text="",font=("ariel",60,"bold")) #word
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

#buttons
next_button = Button(image=right_button_img, highlightthickness=0,command=next_card)
next_button.grid(column=1,row=2)

wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(column=0,row=2)






next_card()
window.mainloop()

