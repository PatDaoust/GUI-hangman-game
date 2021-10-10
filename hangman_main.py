# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:41:29 2021

@author: catal
"""

import tkinter as tk
from PIL import ImageTk, Image
import random
from tkinter.filedialog import askopenfilename


def letterPress(letter, button):
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue(f"You have selected the letter {letter}")
    button["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + letter)
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if letter in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


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


def is_word_guessed():
    '''
    assumes secret word is a string, representing the word the user is guessing
    and that all the letters are lowercase
    assumes letters_guessed is a string individual lowercase letters
    returns a boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    shared_characters = ""
    # filled out shared_characters string
    for char in secret_word.get():
        if char in letters_guessed.get():
            shared_characters = shared_characters + char
    # compare
    if shared_characters == secret_word.get():
        return True
    else:
        return False


def endGame():
    "deactivates all buttons, ending the game"
    for button in letter_buttons_list:
        button["state"] = "disabled"


def lose_game():
    """run to generate losing end game code, when guesses_remaining==0"""
    updateDialogue(f"Sorry, you ran out of guesses. \nThe word was {secret_word.get()}.")
    endGame()


def win_game():
    """run to generate wining end game code,
    when is_word_guessed(secret_word, letters_guessed) returns True"""
    score = guesses_remaining.get() * secret_word_lenght.get()
    updateDialogue(f"Congratulations, you won!\nYour total score for this game is: {score}")
    hangman_img_label["image"] = balloons_image
    endGame()


def get_guessed_word():
    '''
    updates word_label's text, representing the guess so far with the letters that have
    been guessed, and a underscore space (_ ) for the unguessed letters
    '''
    guessed_word_list = ["_ "]*len(secret_word.get())
    # replaced guessed letters into list
    var_index = 0
    for char in secret_word.get():
        if char in letters_guessed.get():
            guessed_word_list[var_index] = char
            var_index += 1
        else:
            var_index += 1
    # convert list to string
    guessed_word = ""
    for ele in guessed_word_list:
        guessed_word += ele
    word_label["text"] = guessed_word


def next_round():
    """
    assumes guesses_remaining is an int
    assumes secret_word is a string
    assumes letters_guessed is a list of characters
    plays out a standard round.
    updates guessed_letter"""
    get_guessed_word()
    updateDialogue("Please guess your next letter.")


def updatePicture():
    """updates the hangman_images based on guesses_remaining"""
    images_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6]
    hangman_img_label["image"] = images_list[guesses_remaining.get()]


def updateDialogue(new_text):
    """updates the dialogue boxes, shifting the contents"""
    dialogue_label_3["text"] = dialogue_label_2["text"]
    dialogue_label_2["text"] = dialogue_label_1["text"]
    dialogue_label_1["text"] = new_text


def resetGame():
    """resets the game variables and GUI"""
    # reset all buttons
    for button in letter_buttons_list:
        button["state"] = "normal"
    # reset all variables
    secret_word.set(choose_word(load_words()))
    secret_word_lenght.set(len(secret_word.get()))
    guesses_remaining.set(6)
    letters_guessed.set("")
    word_is_guessed.set(False)
    # reset labels
    hangman_img_label["image"] = hangman_6
    word_label["text"] = "_ "*secret_word_lenght.get()
    guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
    updateDialogue("")
    updateDialogue("I've selected a new word")
    updateDialogue(f"I am thinking of a word that is {secret_word_lenght.get()} letters long.")


def popupmsg(msg):
    popup = tk.Tk()
    popup["bg"] = bg_color
    popup.wm_title("Import Instructions")
    label = tk.Label(popup,
                     text=msg,
                     font="Helvetica 30",
                     justify="center",
                     background=bg_color,
                     foreground=active_text_color)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup,
                   text="Okay",
                   font="Helvetica 30",
                   bg=bg_color,
                   fg=active_text_color,
                   relief=tk.RAISED,
                   borderwidth=5,
                   command=lambda: destroyPopupAndGetFileName(popup))
    B1.pack()
    popup.mainloop()


def destroyPopupAndGetFileName(popup):
    popup.destroy()
    global WORDLIST_FILENAME
    WORDLIST_FILENAME = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])


def customWordList():
    """allows user to import a .txt file with their own word list
    selects a word from the user's word list"""
    import_instructions = "You can import your own word list to play with.\nThe file must be in .txt format, and contain only lowercase letters a-z and spaces.\nThe game will use each sequence of letters a-z as a word,\nwith the spaces defining seperate words.\n\nImporting your word list will not untrupt your current game.\nTo start a game with your chosen word list, press reset"
    global WORDLIST_FILENAME
    popupmsg(import_instructions)
    global wordlist
    wordlist = load_words()
    secret_word.set(choose_word(wordlist))


# color scheme variables
active_text_color = "#307C91"
inactive_color = "#B6DCE9"
bg_color = "#C0C0C0"

# create master window
window = tk.Tk()
window.title("Hangman")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window["bg"] = bg_color
icon_photo = ImageTk.PhotoImage(Image.open("hangman_icon.ico"))
window.iconphoto(False, icon_photo)

# initialize gameplay variables
WORDLIST_FILENAME = "words.txt"
secret_word = tk.StringVar(master=window, value=choose_word(load_words()))
secret_word_lenght = tk.IntVar(master=window, value=len(secret_word.get()))
guesses_remaining = tk.IntVar(master=window, value=6)
letters_guessed = tk.StringVar(master=window, value="")
word_is_guessed = tk.BooleanVar(master=window, value=False)

# opening rules
rules_text = """
Your mission is to guess the word.

I will tell you the lenght of the word.
You must press on the letters that you think are in the word.

If you guess wrong, you are penalized one of your 6 guesses.
The letters will conviniently turn themselves off after you press them.

At the end of the game, you will recieve a score.
The less guesses you use up, the higher your score will be.
"""
opening_frame = tk.Frame(master=window, bg=bg_color)
welcome_label_opening = tk.Label(master=opening_frame,
                                 fg=active_text_color,
                                 bg=bg_color,
                                 text="Welcome to Hangman!",
                                 font="Helvetica 70 bold",
                                 width=20,
                                 height=1)
rules_label = tk.Label(master=opening_frame,
                       text=rules_text,
                       fg=active_text_color,
                       bg=bg_color,
                       font="Helvetica 30"
                       )
play_button = tk.Button(master=opening_frame,
                        text="Let's play",
                        font="Helvetica 30",
                        fg=active_text_color,
                        bg=bg_color,
                        relief=tk.RAISED,
                        borderwidth=5,
                        command=opening_frame.destroy
                        )
opening_frame.tkraise()

# create widgets
game_frame = tk.Frame(master=window, bg=bg_color)
frame_left = tk.Frame(master=game_frame, bg=bg_color)
balloons_image = Image.open("balloons3.jpg")
balloons_image = balloons_image.resize((500, 800), Image.NEAREST)
balloons_image = ImageTk.PhotoImage(balloons_image)
hangman_6 = Image.open("500x800 6guesses.jpg")
hangman_6 = hangman_6.resize((500, 800), Image.NEAREST)
hangman_6 = ImageTk.PhotoImage(hangman_6)
hangman_5 = Image.open("500x800 5guesses.jpg")
hangman_5 = hangman_5.resize((500, 800), Image.NEAREST)
hangman_5 = ImageTk.PhotoImage(hangman_5)
hangman_4 = Image.open("500x800 4guesses.jpg")
hangman_4 = hangman_4.resize((500, 800), Image.NEAREST)
hangman_4 = ImageTk.PhotoImage(hangman_4)
hangman_3 = Image.open("500x800 3guesses.jpg")
hangman_3 = hangman_3.resize((500, 800), Image.NEAREST)
hangman_3 = ImageTk.PhotoImage(hangman_3)
hangman_2 = Image.open("500x800 2guesses.jpg")
hangman_2 = hangman_2.resize((500, 800), Image.NEAREST)
hangman_2 = ImageTk.PhotoImage(hangman_2)
hangman_1 = Image.open("500x800 1guesses.jpg")
hangman_1 = hangman_1.resize((500, 800), Image.NEAREST)
hangman_1 = ImageTk.PhotoImage(hangman_1)
hangman_0 = Image.open("500x800 0guesses.jpg")
hangman_0 = hangman_0.resize((500, 800), Image.NEAREST)
hangman_0 = ImageTk.PhotoImage(hangman_0)
hangman_img_label = tk.Label(master=frame_left,
                             image=hangman_6,
                             width=500,
                             height=800,)
word_label = tk.Label(master=frame_left,
                      fg=active_text_color,
                      bg=bg_color,
                      text="_ "*secret_word_lenght.get(),
                      font="Helvetica 20 bold italic")
guesses_label = tk.Label(master=frame_left,
                         fg=active_text_color,
                         bg=bg_color,
                         text="you have 6 guesses left",
                         font="Helvetica 20")

frame_right = tk.Frame(master=game_frame, bg=bg_color)
welcome_label = tk.Label(master=frame_right,
                         text="Welcome to Hangman!",
                         font="Helvetica 60 bold",
                         fg=active_text_color,
                         bg=bg_color,
                         width=20,
                         height=1)
intro_dialogue = f"Loading word list from file...\nI am thinking of a word that is {secret_word_lenght.get()} letters long."
dialogue_label_1 = tk.Label(master=frame_right,
                            text=intro_dialogue,
                            font="Helvetica 25",
                            fg=active_text_color,
                            bg=bg_color,
                            borderwidth=5,
                            width=43,
                            height=2)
dialogue_label_2 = tk.Label(master=frame_right,
                            font="Helvetica 25",
                            fg=inactive_color,
                            bg=bg_color,
                            borderwidth=5,
                            width=43,
                            height=2)
dialogue_label_3 = tk.Label(master=frame_right,
                            font="Helvetica 25",
                            fg=inactive_color,
                            bg=bg_color,
                            borderwidth=5,
                            width=43,
                            height=2)
availabe_letters_label = tk.Label(master=frame_right,
                                  fg=active_text_color,
                                  bg=bg_color,
                                  text="available letters",
                                  font="Helvetica 20 italic")
letters_frame = tk.Frame(master=frame_right,
                         borderwidth=5,
                         relief=tk.SUNKEN,
                         bg=bg_color)

reset_import_frame = tk.Frame(master=frame_right, bg=bg_color)
import_button = tk.Button(master=reset_import_frame,
                          text="Import\nWordlist",
                          font="Helvetica 20",
                          fg=active_text_color,
                          bg=bg_color,
                          borderwidth=5,
                          relief=tk.RAISED,
                          width=6,
                          height=1,
                          command=customWordList)
reset_button = tk.Button(master=reset_import_frame,
                         text="Reset\nGame",
                         font="Helvetica 20",
                         fg=active_text_color,
                         bg=bg_color,
                         borderwidth=5,
                         relief=tk.RAISED,
                         width=6,
                         height=1,
                         command=resetGame)


# grid widgets
opening_frame.grid(row=0, column=0, sticky="nsew")
welcome_label_opening.pack()
rules_label.pack()
play_button.pack()
opening_frame.tkraise(game_frame)
game_frame.grid(row=0, column=0)

frame_left.grid(row=0, column=0)
hangman_img_label.grid(row=0, column=0)
word_label.grid(row=1, column=0)
guesses_label.grid(row=2, column=0)

frame_right.grid(row=0, column=1)
welcome_label.grid(row=0, column=0, sticky="n", columnspan=2)
dialogue_label_1.grid(row=3, column=0, columnspan=2)
dialogue_label_2.grid(row=2, column=0, columnspan=2)
dialogue_label_3.grid(row=1, column=0, columnspan=2)
availabe_letters_label.grid(row=4, column=0)
letters_frame.grid(row=5, column=0)

reset_import_frame.grid(row=5, column=1, sticky="sw")
import_button.grid(row=0, column=0, sticky="sw", pady=10)
reset_button.grid(row=1, column=0, sticky="sw", pady=10)

# create and grid letter buttons
button_a = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="a",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("a", button_a)
                     )
button_b = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="b",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("b", button_b)
                     )
button_c = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="c",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("c", button_c)
                     )
button_d = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="d",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("d", button_d)
                     )
button_e = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="e",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("e", button_e)
                     )
button_f = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="f",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("f", button_f)
                     )
button_g = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="g",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("g", button_g)
                     )
button_h = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="h",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("h", button_h)
                     )
button_i = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="i",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("i", button_i)
                     )
button_j = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="j",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("j", button_j)
                     )
button_k = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="k",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("k", button_k)
                     )
button_l = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="l",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("l", button_l)
                     )
button_m = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="m",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("m", button_m)
                     )
button_n = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="n",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("n", button_n)
                     )
button_o = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="o",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("o", button_o)
                     )
button_p = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="p",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("p", button_p)
                     )
button_q = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="q",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("q", button_q)
                     )
button_r = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="r",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("r", button_r)
                     )
button_s = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="s",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("s", button_s)
                     )
button_t = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="t",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("t", button_t)
                     )
button_u = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="u",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("u", button_u)
                     )
button_v = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="v",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("v", button_v)
                     )
button_w = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="w",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("w", button_w)
                     )
button_x = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="x",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("x", button_x)
                     )
button_y = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="y",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("y", button_y)
                     )
button_z = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 25 bold",
                     text="z",
                     fg=active_text_color,
                     bg=bg_color,
                     disabledforeground=inactive_color,
                     command=lambda: letterPress("z", button_z)
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

letter_buttons_list = [button_a,
                       button_b,
                       button_c,
                       button_d,
                       button_e,
                       button_f,
                       button_g,
                       button_h,
                       button_i,
                       button_j,
                       button_k,
                       button_l,
                       button_m,
                       button_n,
                       button_o,
                       button_p,
                       button_q,
                       button_r,
                       button_s,
                       button_t,
                       button_u,
                       button_v,
                       button_w,
                       button_x,
                       button_y,
                       button_z]

window.mainloop()

# TODO dynamic resizing OR smaller play window
# option 2 go through and manually resize everything, add weight param
