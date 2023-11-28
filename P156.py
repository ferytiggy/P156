# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:34:42 2023

@author: Aidan
"""

from tkinter import*

from PIL import ImageTk, Image

root = Tk()

root.title("P156")

root.geometry("600x600")

root.configure(background="lime")

jugador1 = Label(root, text="Jugador 1", bg="White", fg="Black")

jugador1.place(relx=0.1, rely=0.3, anchor=CENTER)

Botón1 = Label(root, bg="Black")

Botón1.place(relx=0.1, rely=0.4, anchor=CENTER)

jugador2 = Label(root, text="Jugador 2", bg="Black", fg="White")

jugador2.place(relx=0.9, rely=0.3, anchor=CENTER)

Boton2 = Label(root, bg="White")

Boton2.place(relx=0.9, rely=0.4, anchor=CENTER)

Numero = Label(root, bg="yellow", fg="Black")

Numero.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()