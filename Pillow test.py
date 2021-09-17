
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

hangman_images = ImageTk.PhotoImage(Image.open("hangman pics.jpg"))
my_label = tk.Label(image=my_img)

my_label.pack()

window.mainloop()
