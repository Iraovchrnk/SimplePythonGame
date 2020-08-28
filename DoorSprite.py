from Sprite import *
from Coords import *
from tkinter import *


class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.closed_door = PhotoImage(file="figures/door1.gif")
        self.open_door = PhotoImage(file="figures/door2.gif")
        self.coordinates = Coords(x, y, x + width/2, y + height)
        self.endgame = True

    def opendoor(self):
        self.game.canvas.itemconfig(self.image, image=self.open_door)
        self.game.tk.update_idletasks()

    def closedoor(self):
        self.game.canvas.itemconfig(self.image, image=self.closed_door)
        self.game.tk.update_idletasks()
