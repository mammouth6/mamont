from tkinter import *

root = Tk()

root.geometry('230x470+100+100')

root.resizable(width=False, height=False)

lbl = Label (text = " ",justify = "center",font = "Calibri 16 bold")
e = Entry (text = " ",justify = "center", font = "Calibri 16 ")

def out_text_red():
    e.delete(0, END)
    lbl["text"] = "Красный"
    e.insert (0, "#ff0000")
def out_text_orange():
    e.delete(0, END)
    lbl["text"] = "Ораньжевый"
    e.insert (0, "#ff7d00")
def out_text_yellow():
    e.delete(0, END)
    lbl["text"] = "Желтый"
    e.insert (0, "#ffff00")
def out_text_green():
    e.delete(0, END)
    lbl["text"] = "Зеленый"
    e.insert (0, "##00ff00")
def out_text_lightblue():
    e.delete(0, END)
    lbl["text"] = "Голубой"
    e.insert (0, "#007dff")
def out_text_blue():
    e.delete(0, END)
    lbl["text"] = "Синий"
    e.insert (0, "#0000ff")
def out_text_purple():
    e.delete(0, END)
    lbl["text"] = "Фиолетовый"
    e.insert (0, "#7d00ff")

b1 = Button(width = 22,height = 3,bg = '#ff0000',command = out_text_red)
b2 = Button(width = 22,height = 3,bg = '#ff7d00',command = out_text_orange)
b3 = Button(width = 22,height = 3,bg = '#ffff00',command = out_text_yellow)
b4 = Button(width = 22,height = 3,bg = '#00ff00',command = out_text_green)
b5 = Button(width = 22,height = 3,bg = '#007dff',command = out_text_lightblue)
b6 = Button(width = 22,height = 3,bg = '#0000ff',command = out_text_blue)
b7 = Button(width = 22,height = 3,bg = '#7d00ff',command = out_text_purple)

lbl.pack()
e.pack()

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

root.mainloop()
