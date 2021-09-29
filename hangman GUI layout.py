# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:41:29 2021

@author: catal
"""

import tkinter as tk
from PIL import ImageTk, Image
import random
import string


def letterPressA():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter a"
    print(letters_guessed.get())
    letters_guessed.set(letters_guessed.get() + "a")
    print(letters_guessed.get())
    # TODO check if word guessed w/letter


def letterPressB():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter b"


def letterPressC():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter c"


def letterPressD():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter d"


def letterPressE():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter e"


def letterPressF():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter f"


def letterPressG():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter g"


def letterPressH():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter h"


def letterPressI():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter i"


def letterPressJ():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter j"


def letterPressK():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter k"


def letterPressL():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter l"


def letterPressM():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter m"


def letterPressN():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter n"


def letterPressO():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter o"


def letterPressP():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter p"


def letterPressQ():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter q"


def letterPressR():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter r"


def letterPressS():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter s"


def letterPressT():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter t"


def letterPressU():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter u"


def letterPressV():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter v"


def letterPressW():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter w"


def letterPressX():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter x"


def letterPressY():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter y"


def letterPressZ():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    dialogue_label["text"] = "You have selected the letter z"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    assumes wordlist is a list of strings, representing words
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    assumes secret word is a string, representing the word the user is guessing
    and that all the letters are lowercase
    assumes letters_guessed is a list individual lowercase letters
    returns a boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    shared_characters = ""
    # filled out shared_characters string
    for char in secret_word:
        if char in letters_guessed:
            shared_characters = shared_characters + char
    # compare strings
    if shared_characters == secret_word:
        return True
    else:
        return False


# create master window
window = tk.Tk()
window.title("hangman layout")
window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
icon_photo = ImageTk.PhotoImage(Image.open("hangman icon.jpg"))
window.iconphoto(False, icon_photo)


# initialize gameplay variables
WORDLIST_FILENAME = "words.txt"
secret_word = tk.StringVar(master=window, value=choose_word(load_words()))
secret_word_lenght = tk.IntVar(master=window, value=len(secret_word.get()))
guesses_remaining = tk.IntVar(master=window, value=6)
letters_guessed = tk.StringVar(master=window, value="letters")

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
                      text="_ "*secret_word_lenght.get(),
                      font="Helvetica 25 bold italic")
guesses_label = tk.Label(master=frame_left,
                         text="you have 6 guesses left",
                         font="Helvetica 25")

frame_right = tk.Frame(master=window)
welcome_label = tk.Label(master=frame_right,
                         text="Welcome to Hangman!",
                         font="Helvetica 70 bold",
                         width=20,
                         height=2)
intro_dialogue = f"Loading word list from file...\nI am thinking of a word that is {secret_word_lenght.get()} letters long."
dialogue_label = tk.Label(master=frame_right,
                          text=intro_dialogue,
                          font="Helvetica 30",
                          borderwidth=5,
                          relief=tk.SUNKEN,
                          width=40,
                          height=3)
# TODO setup dialogue box to show current dialogue in black, previous dialogue in gray
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
button_a = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="a",
                     command=letterPressA
                     )
button_b = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="b",
                     command=letterPressB
                     )
button_c = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="c",
                     command=letterPressC
                     )
button_d = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="d",
                     command=letterPressD
                     )
button_e = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="e",
                     command=letterPressE
                     )
button_f = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="f",
                     command=letterPressF
                     )
button_g = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="g",
                     command=letterPressG
                     )
button_h = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="h",
                     command=letterPressH
                     )
button_i = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="i",
                     command=letterPressI
                     )
button_j = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="j",
                     command=letterPressJ
                     )
button_k = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="k",
                     command=letterPressK
                     )
button_l = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="l",
                     command=letterPressL
                     )
button_m = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="m",
                     command=letterPressM
                     )
button_n = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="n",
                     command=letterPressN
                     )
button_o = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="o",
                     command=letterPressO
                     )
button_p = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="p",
                     command=letterPressP
                     )
button_q = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="q",
                     command=letterPressQ
                     )
button_r = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="r",
                     command=letterPressR
                     )
button_s = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="s",
                     command=letterPressS
                     )
button_t = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="t",
                     command=letterPressT
                     )
button_u = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="u",
                     command=letterPressU
                     )
button_v = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="v",
                     command=letterPressV
                     )
button_w = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="w",
                     command=letterPressW
                     )
button_x = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="x",
                     command=letterPressX
                     )
button_y = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="y",
                     command=letterPressY
                     )
button_z = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="z",
                     command=letterPressZ
                     )

button_a.grid(row=0, column=0, padx=10, pady=10)
button_b.grid(row=0, column=1, padx=10, pady=10)
button_c.grid(row=0, column=2, padx=10, pady=10)
button_d.grid(row=0, column=3, padx=10, pady=10)
button_e.grid(row=0, column=4, padx=10, pady=10)
button_f.grid(row=0, column=5, padx=10, pady=10)
button_g.grid(row=0, column=6, padx=10, pady=10)
button_h.grid(row=0, column=7, padx=10, pady=10)
button_i.grid(row=0, column=8, padx=10, pady=10)
button_j.grid(row=1, column=0, padx=10, pady=10)
button_k.grid(row=1, column=1, padx=10, pady=10)
button_l.grid(row=1, column=2, padx=10, pady=10)
button_m.grid(row=1, column=3, padx=10, pady=10)
button_n.grid(row=1, column=4, padx=10, pady=10)
button_o.grid(row=1, column=5, padx=10, pady=10)
button_p.grid(row=1, column=6, padx=10, pady=10)
button_q.grid(row=1, column=7, padx=10, pady=10)
button_r.grid(row=2, column=0, padx=10, pady=10)
button_s.grid(row=2, column=1, padx=10, pady=10)
button_t.grid(row=2, column=2, padx=10, pady=10)
button_u.grid(row=2, column=3, padx=10, pady=10)
button_v.grid(row=2, column=4, padx=10, pady=10)
button_w.grid(row=2, column=5, padx=10, pady=10)
button_x.grid(row=2, column=6, padx=10, pady=10)
button_y.grid(row=2, column=7, padx=10, pady=10)
button_z.grid(row=2, column=8, padx=10, pady=10)

# TODO deactivate buttons when pressed
# tk.event.widget to call widget that set off event

window.mainloop()
