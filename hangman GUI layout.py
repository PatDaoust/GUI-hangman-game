# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:41:29 2021

@author: catal
"""

import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("hangman layout")
window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

# TODO add icon image

# create widgets
frame_left = tk.Frame(master=window)
hangman_images = Image.open("hangman6Guesses.jpg")
hangman_images = hangman_images.resize((500, 800), Image.NEAREST)
hangman_images = ImageTk.PhotoImage(hangman_images)
hangman_img_label = tk.Label(master=frame_left,
                             image=hangman_images,
                             width=500,
                             height=800,)
word_label = tk.Label(master=frame_left,
                      text="_ _ _ _ _",
                      font="Helvetica 30 bold italic")
guesses_label = tk.Label(master=frame_left,
                         text="you have 6 guesses left",
                         font="Helvetica 30")

frame_right = tk.Frame(master=window)
welcome_label = tk.Label(master=frame_right,
                         text="Welcome to Hangman!",
                         font="Helvetica 80 bold",
                         width=20,
                         height=2)
dialogue_label = tk.Label(master=frame_right,
                          text="this is where dialogue goes",
                          font="Helvetica 30",
                          borderwidth=5,
                          relief=tk.SUNKEN,
                          width=50,
                          height=3)
availabe_letters_label = tk.Label(master=frame_right,
                                  text="available letters",
                                  font="Helvetica 20 italic")
letters_frame = tk.Frame(master=frame_right)

# grid widgets
frame_left.grid(row=0, column=0)
hangman_img_label.grid(row=0, column=0)  # sticky="nsew"
word_label.grid(row=1, column=0)
guesses_label.grid(row=2, column=0)

frame_right.grid(row=0, column=1)
welcome_label.grid(row=0, column=0, sticky="n")
dialogue_label.grid(row=1, column=0)
availabe_letters_label.grid(row=2, column=0)
letters_frame.grid(row=3, column=0)

# create and grid letter buttons
i = 0
j = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    button = tk.Button(master=letters_frame,
                       text=letter,
                       relief=tk.RAISED,
                       borderwidth=5,
                       font="Helvetica 30 bold"
                       # TODO padding, here or in grid?
                       )
    button.grid(row=j, column=i)
    i += 1
    if i > 8:
        i = 0
        j += 1


window.mainloop()