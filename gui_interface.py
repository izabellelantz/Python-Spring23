"""
Program: gui_interface.py
Name: Izabelle Lantz
Date: 03/22/2023
The purpose of this program is to create a GUI where a widget will pop up
to ask user for their choice of favorite meal of the day. Once they respond, a trigger
event will cause the widget to tell the user they made a great choice.
"""
import tkinter


def on_click():
    label.config(text='Good Choice!')


m = tkinter.Tk()
m.title('Favorite Meal')
label = tkinter.Label(m, text='Waiting')
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text='Breakfast', variable=var1, command=on_click).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text='Second Breakfast', variable=var2, command=on_click).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text='Lunch', variable=var3, command=on_click).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text='Dinner', variable=var4, command=on_click).grid(row=4)
button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
button.grid(row=6)
m.mainloop()