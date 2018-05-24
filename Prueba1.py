from tkinter import *
import pygame

pygame.init()
pygame.mixer.music.load('cancion.mp3')
pygame.mixer.music.play(-1, 0.0)
musicaplay = True

tk=Tk()
canvas=Canvas(tk,width=1000, height=800)
canvas.pack()

my_image=PhotoImage(file="fondo3.gif")
canvas.create_image(0,0,anchor=NW,image=my_image)

my_image2=PhotoImage(file="porteria3.gif")
canvas.create_image(0,0,anchor=NW,image=my_image2)

my_image1 = PhotoImage(file="balon1.gif")
canvas.create_image(825, 625, anchor=NW, image=my_image1)

my_image3 = PhotoImage(file="gol1.gif")
canvas.create_image(400, 0, anchor=NW, image=my_image3)

def movebalon(event):
    canvas.move(3, 5, 0)

def movebalon1(event):
    canvas.move(3, -5, 0)


def movebalon2(event):
    canvas.move(3, 0, -5)

def movebalon3(event):
    canvas.move(3, 0, 5)

canvas.bind_all("<KeyPress-Left>", movebalon1)
canvas.bind_all("<KeyPress-Right>", movebalon)
canvas.bind_all("<KeyPress-Up>", movebalon2)
canvas.bind_all("<KeyPress-Down>", movebalon3)


tk.mainloop()

