# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:41:29 2021

@author: catal
"""

import tkinter as tk
from PIL import ImageTk, Image
import random


def letterPressA():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter a")
    button_a["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "a")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "a" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressB():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter b")
    button_b["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "b")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "b" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressC():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter c")
    button_c["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "c")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "c" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressD():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter d")
    button_d["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "d")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "d" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressE():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter e")
    button_e["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "e")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "e" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressF():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter f")
    button_f["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "f")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "f" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressG():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter g")
    button_g["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "g")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "g" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressH():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter h")
    button_h["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "h")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "h" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressI():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter i")
    button_i["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "i")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "i" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressJ():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter j")
    button_j["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "j")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "j" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressK():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter k")
    button_k["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "k")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "k" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressL():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter l")
    button_l["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "l")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "l" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressM():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter m")
    button_m["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "m")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "m" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressN():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter n")
    button_n["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "n")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "n" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressO():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter o")
    button_o["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "o")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "o" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressP():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter p")
    button_p["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "p")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "p" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressQ():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter q")
    button_q["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "q")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "q" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressR():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter r")
    button_r["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "r")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "r" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressS():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter s")
    button_s["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "s")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "s" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressT():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter t")
    button_t["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "t")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "t" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressU():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter u")
    button_u["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "u")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "u" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressV():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter v")
    button_v["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "v")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "v" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressW():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter w")
    button_w["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "w")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "w" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressX():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letterx ")
    button_x["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "x")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "x" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressY():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter y")
    button_y["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "y")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "y" in secret_word.get():
            updateDialogue("Good guess!")
        else:
            updateDialogue("Bad guess. You've been penalized a guess")
            guesses_remaining.set(guesses_remaining.get()-1)
            guesses_label["text"] = f"you have {guesses_remaining.get()} guesses left"
            if guesses_remaining.get() <= 0:
                lose_game()
        updatePicture()


def letterPressZ():
    """assumes letter is a char in "abcdefghijklmnopqrstuvwxyz"
    submits the letter to the game
    """
    updateDialogue("You have selected the letter z")
    button_z["state"] = "disabled"
    letters_guessed.set(letters_guessed.get() + "z")
    word_is_guessed.set(is_word_guessed())
    next_round()
    did_win = is_word_guessed()
    if did_win:
        win_game()
    else:
        if "z" in secret_word.get():
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
    button_a["state"] = "disabled"
    button_b["state"] = "disabled"
    button_c["state"] = "disabled"
    button_d["state"] = "disabled"
    button_e["state"] = "disabled"
    button_f["state"] = "disabled"
    button_g["state"] = "disabled"
    button_h["state"] = "disabled"
    button_i["state"] = "disabled"
    button_j["state"] = "disabled"
    button_k["state"] = "disabled"
    button_l["state"] = "disabled"
    button_m["state"] = "disabled"
    button_n["state"] = "disabled"
    button_o["state"] = "disabled"
    button_p["state"] = "disabled"
    button_q["state"] = "disabled"
    button_r["state"] = "disabled"
    button_s["state"] = "disabled"
    button_t["state"] = "disabled"
    button_u["state"] = "disabled"
    button_v["state"] = "disabled"
    button_w["state"] = "disabled"
    button_x["state"] = "disabled"
    button_y["state"] = "disabled"
    button_z["state"] = "disabled"


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
# secret_word = tk.StringVar(master=window, value=choose_word(load_words()))
secret_word = tk.StringVar(master=window, value="cats")  # TODO randomize
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
opening_frame = tk.Frame(master=window)
welcome_label_opening = tk.Label(master=opening_frame,
                                 text="Welcome to Hangman!",
                                 font="Helvetica 70 bold",
                                 width=20,
                                 height=1)
rules_label = tk.Label(master=opening_frame,
                       text=rules_text,
                       font="Helvetica 30"
                       )
play_button = tk.Button(master=opening_frame,
                        text="Let's play",
                        font="Helvetica 30",
                        relief=tk.RAISED,
                        borderwidth=5,
                        command=opening_frame.destroy
                        )
opening_frame.tkraise()

# create widgets
game_frame = tk.Frame(master=window)
frame_left = tk.Frame(master=game_frame)
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
                      text="_ "*secret_word_lenght.get(),
                      font="Helvetica 25 bold italic")
guesses_label = tk.Label(master=frame_left,
                         text="you have 6 guesses left",
                         font="Helvetica 25")

frame_right = tk.Frame(master=game_frame)
welcome_label = tk.Label(master=frame_right,
                         text="Welcome to Hangman!",
                         font="Helvetica 70 bold",
                         width=20,
                         height=1)
intro_dialogue = f"Loading word list from file...\nI am thinking of a word that is {secret_word_lenght.get()} letters long."
dialogue_label_1 = tk.Label(master=frame_right,
                            text=intro_dialogue,
                            font="Helvetica 30",
                            borderwidth=5,
                            relief=tk.SUNKEN,
                            width=43,
                            height=2)
dialogue_label_2 = tk.Label(master=frame_right,
                            font="Helvetica 30",
                            fg="#D0D4D6",
                            borderwidth=5,
                            relief=tk.SUNKEN,
                            width=43,
                            height=2)
dialogue_label_3 = tk.Label(master=frame_right,
                            font="Helvetica 30",
                            fg="#D0D4D6",
                            borderwidth=5,
                            relief=tk.SUNKEN,
                            width=43,
                            height=2)
availabe_letters_label = tk.Label(master=frame_right,
                                  text="available letters",
                                  font="Helvetica 20 italic")
letters_frame = tk.Frame(master=frame_right,
                         borderwidth=5,
                         relief=tk.SUNKEN)

reset_import_frame = tk.Frame(master=frame_right)
import_button = tk.Button(master=reset_import_frame,
                          text="Import\nWordlist",
                          font="Helvetica 30",
                          borderwidth=5,
                          relief=tk.RAISED,
                          width=6,
                          height=1)
reset_button = tk.Button(master=reset_import_frame,
                         text="Reset\nGame",
                         font="Helvetica 30",
                         borderwidth=5,
                         relief=tk.RAISED,
                         width=6,
                         height=1)


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
                     font="Helvetica 30 bold",
                     text="a",
                     disabledforeground="#D0D4D6",
                     command=letterPressA
                     )
button_b = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="b",
                     disabledforeground="#D0D4D6",
                     command=letterPressB
                     )
button_c = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="c",
                     disabledforeground="#D0D4D6",
                     command=letterPressC
                     )
button_d = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="d",
                     disabledforeground="#D0D4D6",
                     command=letterPressD
                     )
button_e = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="e",
                     disabledforeground="#D0D4D6",
                     command=letterPressE
                     )
button_f = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="f",
                     disabledforeground="#D0D4D6",
                     command=letterPressF
                     )
button_g = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="g",
                     disabledforeground="#D0D4D6",
                     command=letterPressG
                     )
button_h = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="h",
                     disabledforeground="#D0D4D6",
                     command=letterPressH
                     )
button_i = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="i",
                     disabledforeground="#D0D4D6",
                     command=letterPressI
                     )
button_j = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="j",
                     disabledforeground="#D0D4D6",
                     command=letterPressJ
                     )
button_k = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="k",
                     disabledforeground="#D0D4D6",
                     command=letterPressK
                     )
button_l = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="l",
                     disabledforeground="#D0D4D6",
                     command=letterPressL
                     )
button_m = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="m",
                     disabledforeground="#D0D4D6",
                     command=letterPressM
                     )
button_n = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="n",
                     disabledforeground="#D0D4D6",
                     command=letterPressN
                     )
button_o = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="o",
                     disabledforeground="#D0D4D6",
                     command=letterPressO
                     )
button_p = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="p",
                     disabledforeground="#D0D4D6",
                     command=letterPressP
                     )
button_q = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="q",
                     disabledforeground="#D0D4D6",
                     command=letterPressQ
                     )
button_r = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="r",
                     disabledforeground="#D0D4D6",
                     command=letterPressR
                     )
button_s = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="s",
                     disabledforeground="#D0D4D6",
                     command=letterPressS
                     )
button_t = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="t",
                     disabledforeground="#D0D4D6",
                     command=letterPressT
                     )
button_u = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="u",
                     disabledforeground="#D0D4D6",
                     command=letterPressU
                     )
button_v = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="v",
                     disabledforeground="#D0D4D6",
                     command=letterPressV
                     )
button_w = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="w",
                     disabledforeground="#D0D4D6",
                     command=letterPressW
                     )
button_x = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="x",
                     disabledforeground="#D0D4D6",
                     command=letterPressX
                     )
button_y = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="y",
                     disabledforeground="#D0D4D6",
                     command=letterPressY
                     )
button_z = tk.Button(master=letters_frame,
                     relief=tk.RAISED,
                     borderwidth=5,
                     font="Helvetica 30 bold",
                     text="z",
                     disabledforeground="#D0D4D6",
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

# TODO implement reset button
# TODO implement option to import own word list
# TODO write single letterPress() function, use lambda function on button command
# TODO try alternaqtive color scheme
# TODO make .exe file to send out

window.mainloop()
