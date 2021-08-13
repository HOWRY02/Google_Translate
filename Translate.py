from tkinter import*
import tkinter.ttk as exTk
from PIL import Image, ImageTk
import googletrans
from googletrans import Translator

root = Tk()
root.title('Google Galaxy')
root.geometry('500x630')
root.iconbitmap("logo.ico")

load = Image.open("background.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#01142C")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

keys = list(googletrans.LANGUAGES.values())
values = list(googletrans.LANGUAGES.keys())
adict = dict(zip(keys, values))

combo = exTk.Combobox(root)
combo['value'] = tuple(keys)
combo.pack(pady=0)

box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=10)

combo1 = exTk.Combobox(root)
combo1['value'] = tuple(keys)
combo1.place(x=180, y=360)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)
def translate():
    box1.delete(1.0, END)
    INPUT = box.get(1.0, END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, src=adict[combo.get()], dest=adict[combo1.get()])
    b = a.text
    box1.insert(END, b)

clear_button = Button(button_frame, text="Clear text", font=(("Arial"),10,"bold"), bg="#303030", fg="#FFFFFF", command=clear)
clear_button.place(x=150, y=320)
trans_button = Button(button_frame, text="Translate", font=(("Arial"),10,"bold"), bg="#303030", fg="#FFFFFF", command=translate)
trans_button.place(x=290, y=320)

box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.place(x=80,y=390)

root.mainloop()
