# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:41:29 2021

@author: catal
"""

import tkinter as tk
from PIL import ImageTk, Image


def letterPress():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter " + "a"


window = tk.Tk()
window.title("hangman layout")
window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

# TODO add icon image

# create widgets
frame_left = tk.Frame(master=window)  #TODO try adjusting frame size to fix lettering
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
                         font="Helvetica 70 bold",
                         width=20,
                         height=2)
dialogue_label = tk.Label(master=frame_right,
                          text="this is where dialogue goes",
                          font="Helvetica 30",
                          borderwidth=5,
                          relief=tk.SUNKEN,
                          width=40,
                          height=3)
availabe_letters_label = tk.Label(master=frame_right,
                                  text="available letters",
                                  font="Helvetica 20 italic")
letters_frame = tk.Frame(master=frame_right)

# grid widgets
frame_left.grid(row=0, column=0)
hangman_img_label.grid(row=0, column=0)
word_label.grid(row=1, column=0)
guesses_label.grid(row=2, column=0)

frame_right.grid(row=0, column=1)
welcome_label.grid(row=0, column=0, sticky="n")
dialogue_label.grid(row=1, column=0)
availabe_letters_label.grid(row=2, column=0)
letters_frame.grid(row=3, column=0)

# create and grid letter buttons
button_content = button = tk.Button(master=letters_frame,
                                    relief=tk.RAISED,
                                    borderwidth=5,
                                    font="Helvetica 30 bold",
                                    bg="aqua",
                                    command=letterPress
                                    )
button_a = button_content
button_b = button_content
# button_c = button_content
# button_d = button_content
# button_e = button_content
# button_f = button_content
# button_g = button_content
# button_h = button_content
# button_i = button_content
# button_j = button_content
# button_k = button_content
# button_l = button_content
# button_m = button_content
# button_n = button_content
# button_o = button_content
# button_p = button_content
# button_q = button_content
# button_r = button_content
# button_s = button_content
# button_t = button_content
# button_u = button_content
# button_v = button_content
# button_w = button_content
# button_x = button_content
# button_y = button_content
# button_z = button_content

button_a["text"] = "a"
button_b["text"] = "b"
# button_c["text"] = "c"
# button_d["text"] = "d"
# button_e["text"] = "e"
# button_f["text"] = "f"
# button_g["text"] = "g"
# button_h["text"] = "h"
# button_i["text"] = "i"
# button_j["text"] = "j"
# button_k["text"] = "k"
# button_l["text"] = "l"
# button_m["text"] = "m"
# button_n["text"] = "n"
# button_o["text"] = "o"
# button_p["text"] = "p"
# button_q["text"] = "q"
# button_r["text"] = "r"
# button_s["text"] = "s"
# button_t["text"] = "t"
# button_u["text"] = "u"
# button_v["text"] = "v"
# button_w["text"] = "w"
# button_x["text"] = "x"
# button_y["text"] = "y"
# button_z["text"] = "z"

button_a.grid(row=0, column=0, padx=10, pady=10)
button_b.grid(row=0, column=1, padx=10, pady=10)
# button_c.grid(row=0, column=2, padx=10, pady=10)
# button_d.grid(row=0, column=3, padx=10, pady=10)
# button_e.grid(row=0, column=4, padx=10, pady=10)
# button_f.grid(row=0, column=5, padx=10, pady=10)
# button_g.grid(row=0, column=6, padx=10, pady=10)
# button_h.grid(row=0, column=7, padx=10, pady=10)
# button_i.grid(row=0, column=8, padx=10, pady=10)
# button_j.grid(row=1, column=0, padx=10, pady=10)
# button_k.grid(row=1, column=1, padx=10, pady=10)
# button_l.grid(row=1, column=2, padx=10, pady=10)
# button_m.grid(row=1, column=3, padx=10, pady=10)
# button_n.grid(row=1, column=4, padx=10, pady=10)
# button_o.grid(row=1, column=5, padx=10, pady=10)
# button_p.grid(row=1, column=6, padx=10, pady=10)
# button_q.grid(row=1, column=7, padx=10, pady=10)
# button_r.grid(row=2, column=0, padx=10, pady=10)
# button_s.grid(row=2, column=1, padx=10, pady=10)
# button_t.grid(row=2, column=2, padx=10, pady=10)
# button_u.grid(row=2, column=3, padx=10, pady=10)
# button_v.grid(row=2, column=4, padx=10, pady=10)
# button_w.grid(row=2, column=5, padx=10, pady=10)
# button_x.grid(row=2, column=6, padx=10, pady=10)
# button_y.grid(row=2, column=7, padx=10, pady=10)
# button_z.grid(row=2, column=8, padx=10, pady=10)

# TODO deactivate buttons when pressed

window.mainloop()
